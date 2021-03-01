from flask import Flask, request, url_for, redirect, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'serveriland@gmail.com',
    "MAIL_PASSWORD": 'i23092005'
}
app.config.update(mail_settings)
mail = Mail(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")



if __name__ == "__main__":
    with app.app_context():
        msg = Message(subject="test",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["shoter998@gmail.com"],
            body="This is test")
        mail.send(msg)
    app.run(debug=True)
