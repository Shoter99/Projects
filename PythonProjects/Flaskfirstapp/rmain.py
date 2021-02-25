from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "fhaghioaejuopabpnaihfiahepfj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
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
            if password == passw:
                session["user"] = found_user.name
                flash("You have been successfully logged in", "info")
                return redirect(url_for("user"))
            else:
                flash("You have typed wrong username or password!", "info")
                return redirect(url_for("login"))
        else:
            flash("You need to register")
            return redirect(url_for("register"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
	found_user = users.query.filter_by(name=user).first()
    if found_user:
        user = found_user.name
        email = found_user.email
        passowrd = found_user.password
        return render_template("user.html", usr=user, email=email, password=passowrd)
    else:
        flash("Please log in before entering this site", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        session.pop("user", None)
        session.pop("pass", None)
        session.pop("register_user", None)
        session.pop("register_password", None)
        session.pop("register_email", None)
        flash("You have been successfully logged out!")
        return redirect(url_for("login"))
    else:
        flash("You need to be logged to log out")
        return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["rUsername"]
        email = request.form["rEmail"]
        password = request.form["rPassword"]
        repassword = request.form["rRepassword"]
        if(password != repassword):
            flash("Passwords must me the same!", "warning")
            redirect(url_for("register"))
        else:
            found_user = users.query.filter_by(name=username).first()
            if found_user:
                flash("Person with this username already exists")
                return render_template("register")
            else:
                usr = users(username, email, password)
                db.session.add(usr)
                db.session.commit()
                flash("Register was successfull!", "info")
                return redirect(url_for("login"))

    return render_template("register.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
