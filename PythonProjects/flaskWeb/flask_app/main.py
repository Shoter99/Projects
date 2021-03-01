from enum import unique
from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "fafhaiohfohaohfa"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datebase.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


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
            found_user = users.query.filter_by(name=user).first()
            if found_user:
                passw = found_user.password
                if passw == password:
                    session["user"] = found_user.name
                    session["email"] = found_user.email
                    session["password"] = found_user.password
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


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        email = session["email"]
        password = session["password"]
        return render_template("user.html", usr=user, email=email, password=password)
    else:
        flash("Please log in before entering this site!")
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
            flash("Passwords must match")
            redirect(url_for("register"))
        else:
            found_user = users.query.filter_by(name=Rusername).first()
            if found_user:
                flash("Person with this name already exits")
                return redirect(url_for("register"))
            else:
                usr = users(Rusername, Remail, Rpassword)
                db.session.add(usr)
                db.session.commit()
                flash("Register has been succesfull!")
                return redirect(url_for("login"))
    else:
        return render_template("register.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
