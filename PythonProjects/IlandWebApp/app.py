from flask import Flask, request, url_for, flash, redirect, render_template, session, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = "dfafageagwa"


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
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        message = request.form["msg"]
        subject = request.form["subject"]
        with app.app_context():
            msg = Message(subject=subject,
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["serveriland@gmail.com"],
            body=f"Od {username}\nEmail: {email}\nWiadomość: {message}")
        mail.send(msg)
        flash("Pomyślnie wysłano wiadomość!")
        return redirect("/")
    else:
        return render_template("index.html")



if __name__ == "__main__":
    
    app.run(debug=True, host="192.168.178.24")
