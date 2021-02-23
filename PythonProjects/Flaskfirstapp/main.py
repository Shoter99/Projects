from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "fhaghioaejuopabpnaihfiahepfj"

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
			if(user == "Shoter99" and password == "d16092003"):
				session["user"] = user
				session["pass"] = password
				return redirect(url_for("user"))
			else:
				#flash
				return redirect(url_for("login"))
		else:
			return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("user.html", usr = user)
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	session.pop("pass", None)
	return redirect(url_for("login"))
if __name__=='__main__':
    app.run(debug=True)
