from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from db_models import Credentials, Users
from db_shared_models import db
from auth import f
records = Blueprint('records', __name__)

@records.route('/deleteRecord', methods=['POST', 'GET'])
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
            return redirect(url_for("routes.user"))
        else:
            return redirect(url_for("routes.user"))

    else:
        flash("You cannot accesss this now!")
        return redirect(url_for("routes.login"))

@records.route('/editRecord', methods=['POST', 'GET'])
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
            return redirect(url_for("routes.user"))
        else:
            return redirect(url_for("routes.user"))
    else:
        flash("You cannot access this right now")
        return redirect(url_for("routes.login"))