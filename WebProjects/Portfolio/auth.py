from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from cryptography.fernet import Fernet
from jinja2.ext import loopcontrols
from db_models import Users, Credentials
import hashlib, os
from db_shared_models import db
routes = Blueprint('routes', __name__)
fkey = b'ZPEMOn-5azg4ftRjiPqywAmhDAuppfO3avZPmUaO5NE='
f = Fernet(fkey)
salt = b'\x92y:B\x84F\x12/W1\x8f\xf0\x9e\x93m\xc5\x89tu\xf0\x19UOy#\x0c:[\xc6=\x06\xef'


@routes.route('/login', methods=['GET', 'POST'])
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
                    return redirect(url_for("routes.user"))
                else:
                    flash("Wrong username or password!")
                    return redirect(url_for("routes.login"))
            else:
                flash(
                    f"In our database there is no user with this name {user}")
                return redirect(url_for("routes.login"))
        else:
            return render_template("login.html")

@routes.route('/user', methods=['GET', 'POST'])
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
                return redirect(url_for("routes.user"))
            found_user = Users.query.filter_by(name=user).first()
            cred = found_user.credentials
            return render_template("user.html", usr=user, crd=cred, f=f)
        else:
            flash("No user found!")
            return redirect(url_for('logout'))
    else:
        flash("Please log in before entering this site!")
        return redirect(url_for("routes.login"))
@routes.route('/register', methods=['POST', 'GET'])
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
            return redirect(url_for("routes.register"))
        else:
            found_user = Users.query.filter_by(name=Rusername).first()
            if found_user:
                flash("Person with this name already exits")
                return redirect(url_for("routes.register"))
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
                return redirect(url_for("routes.login"))
    else:
        return render_template("register.html")

@routes.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("email", None)
    session.pop("password", None)
    flash("You have been succesfully logged out!")
    return redirect(url_for("routes.login"))
