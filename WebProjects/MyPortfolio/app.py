from enum import unique
from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import hashlib, os

token = """
wf57yw3v
7tqynoas
dy6eafwu
gm2uyssl
hyjbc7fc
3tysbu23
g2qeni3r
suvvrggd
hqdoyrtg
aqoh5o2c"""
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "fafhaiohfohaohfa"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datebase.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

fkey = b'ZPEMOn-5azg4ftRjiPqywAmhDAuppfO3avZPmUaO5NE='
f = Fernet(fkey)
salt = b'\x92y:B\x84F\x12/W1\x8f\xf0\x9e\x93m\xc5\x89tu\xf0\x19UOy#\x0c:[\xc6=\x06\xef'
class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    credentials = db.relationship('Credentials', backref='user', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Credentials(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(150))
    url = db.Column(db.String(300))
    app = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, login, password, url, app, user):
        self.login = login
        self.password = password
        self.url = url
        self.app = app
        self.user = user


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if("user" in session):
        return redirect(url_for("user"))
    else:
        if request.method == "POST":
            user = request.form["login"]
            password = request.form["pass"]
            found_user = Users.query.filter_by(name=user).first()
            if found_user:
                passw = found_user.password
                keyToCheck = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,100000)
                if passw == keyToCheck:
                    session["user"] = found_user.name
                    session["email"] = found_user.email
                    session["password"] = password
                    flash("You have been succesfully logged")
                    return redirect(url_for("user"))
                else:
                    flash("Wrong username or password!")
                    return redirect(url_for("login"))
            else:
                flash(
                    f"In our database there is no user with this name {user}")
                return redirect(url_for("login"))
        else:
            return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        email = session["email"]
        password = session["password"]
        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            if request.method == "POST":
                slogin = request.form["slogin"]
                spassword = request.form['spassword']
                surl = request.form['surl']
                sapp = request.form['sapp']
                encp = f.encrypt(spassword.encode('utf-8'))
                credential = Credentials(login=slogin,password=encp,url=surl,app=sapp, user=found_user)
                db.session.add(credential)
                db.session.commit()
                return redirect(url_for("user"))
            found_user = Users.query.filter_by(name=user).first()
            cred = found_user.credentials
            return render_template("user.html", usr=user, crd=cred, f=f)
        else:
            flash("No user found!")
            return redirect(url_for('logout'))
    else:
        flash("Please log in before entering this site!")
        return redirect(url_for("login"))

@app.route("/deleteRecord", methods=["POST", "GET"])
def delete():
    if 'user' in session:
        user = session["user"]
        found_user = Users.query.filter_by(name=user).first()
        if request.method == "POST":
            cred = request.form["creds"]
            print(f'{cred}')
            print(found_user._id)
            found_creds = Credentials.query.filter_by(_id=cred).first()
            db.session.delete(found_creds)
            db.session.commit()
            flash("Record deleted")
            return redirect(url_for("user"))
        else:
            return redirect(url_for("user"))

    else:
        flash("You cannot accesss this now!")
        return redirect(url_for("login"))

@app.route("/editRecord", methods=["POST", "GET"])
def edit():
    if 'user' in session:
        if request.method == "POST":
            cred = request.form['credToEdit']
            login = request.form['loginToEdit']
            password = request.form['passwordToEdit']
            url = request.form['urlToEdit']
            app = request.form['appToEdit']
            found_creds = Credentials.query.filter_by(_id=cred).first()
            found_creds.login = login
            found_creds.password = f.encrypt(password.encode('utf-8'))
            found_creds.url = url
            found_creds.app = app
            db.session.commit()
            flash('Change commited')
            return redirect(url_for("user"))
        else:
            return redirect(url_for("user"))
    else:
        flash("You cannot access this right now")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    session.pop("password", None)
    flash("You have been succesfully logged out!")
    return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        Rusername = request.form["rUsername"]
        Remail = request.form["rEmail"]
        Rpassword = request.form["rPassword"]
        repassword = request.form["rRepassword"]
        session["email"] = Remail
        session["password"] = Rpassword
        if(Rpassword != repassword):
            flash("Password does not match, try again!")
            return redirect(url_for("register"))
        else:
            found_user = Users.query.filter_by(name=Rusername).first()
            if found_user:
                flash("Person with this name already exits")
                return redirect(url_for("register"))
            else:
                key = hashlib.pbkdf2_hmac(
                    'sha256',
                    Rpassword.encode('utf-8'),
                    salt,
                    100000
                    )
                usr = Users(Rusername, Remail, key)
                db.session.add(usr)
                db.session.commit()
                flash("Register has been succesfull!")
                return redirect(url_for("login"))
    else:
        return render_template("register.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0")