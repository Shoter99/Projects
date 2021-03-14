from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from db_models import Questions
from db_shared_models import db
survey = Blueprint('survey', __name__)

@survey.route('/ankieta', methods=['POST', 'GET'])
def ankieta():
    if request.method=="POST":
        if "send" in session:
            return redirect(url_for('survey.finishedSurvey'))
        gender = Questions(request.form['gender'], request.form['q1'],request.form['q2'], request.form['q3'], request.form['q4'],request.form['q5'],request.form['q6'],request.form['q7'],request.form['q8'],request.form['q9'],request.form['q10'],request.form['q11'])
        Questions.q1 = request.form['q1']
        Questions.q2 = request.form['q2']
        db.session.add(gender)
        db.session.commit()
        session["send"] = 'True'
        flash("Ankieta została pomyślnie przesłana </br> Dziękujemy za wypełnienie ankiety!")
        return redirect(url_for('survey.finishedSurvey'))
    else:
        if "send" in session:
            flash("Ankietę możesz wypełnić tylko jeden raz!")
            return redirect(url_for('survey.finishedSurvey'))
        return render_template("ankieta.html")
@survey.route('/finishedSurvey')
def finishedSurvey():
    return render_template('finishedSurvey.html')