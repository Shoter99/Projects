from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "fhaghioaejuopabpnaihfiahepfj"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
	_id = db.Column("id",db.Integer, primary_key=True)
	name = db.Column(db.String(100))

	def __init__(self, name):
		self.name = name


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
			if "register_user" in session:
				user = request.form["login"]
				password = request.form["pass"]
				rUsername = session["register_user"]
				rPassword = session["register_password"]
				if(user == rUsername and password == rPassword):
					session["user"] = user
					session["pass"] = password
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
	if "user" in session:
		user = session["user"]
		username = session["register_user"]
		email =	session["register_email"] 
		passowrd = session["register_password"]
		return render_template("user.html", usr = user, r_user = username, r_email = email, r_password = passowrd)
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
			session["register_user"] = username
			session["register_email"] = email
			session["register_password"] = password
			flash("Register was successfull!","info")
			return redirect(url_for("login"))
	return render_template("register.html")

if __name__=='__main__':
    app.run(debug=True)
