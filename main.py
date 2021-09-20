from flask import Flask, render_template, request
import smtplib
import datetime
import os

my_email = os.environ.get("EMAIL")
my_pass = os.environ.get("PASS")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/#contact", methods=["POST"])
def form():
    if request.method == "POST":
        f_name = request.form.get("f-name")
        l_name = request.form.get("l-name")
        email = request.form.get("email")
        message = request.form.get("message")

        server = smtplib.SMTP("smtp.gmail.com")
        server.starttls()
        server.login(user=my_email, password=my_pass )
        server.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"Subject:Message Received\n\nYou have received a "
                                                                  f"message from ({f_name} {l_name} "
                                                                  f"{email}) with this message: {message}")
        server.close()
        return render_template("mailed.html")

if __name__ == "__main__":
    app.run(debug=True)
