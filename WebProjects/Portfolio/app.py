from enum import unique
from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import hashlib, os
from jinja2.ext import loopcontrols
from auth import routes
from db_shared_models import db
from survey import survey
from managing_records import records
#token = """
#wf57yw3v
#7tqynoas
#dy6eafwu
#gm2uyssl
#hyjbc7fc
#3tysbu23
#g2qeni3r
#suvvrggd
#hqdoyrtg
#aqoh5o2c"""
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "fafhaiohfohaohfa"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///datebase.sqlite3'
app.config["SQLALCHEMY_BINDS"] = {'survey':'sqlite:///survey.sqlite3'}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(routes)
app.register_blueprint(survey)
app.register_blueprint(records)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")

