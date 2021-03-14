from db_shared_models import db

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
class Questions(db.Model):
    __bind_key__ = 'survey'
    _id = db.Column("id", db.Integer, primary_key=True)
    gender = db.Column(db.String(50))
    q1 = db.Column(db.String(20))
    q2 = db.Column(db.String(20))
    q3 = db.Column(db.String(20))
    q4 = db.Column(db.String(20))
    q5 = db.Column(db.String(20))
    q6 = db.Column(db.String(20))
    q7 = db.Column(db.String(20))
    q8 = db.Column(db.String(20))
    q9 = db.Column(db.String(20))
    q10 = db.Column(db.String(20))
    q11 = db.Column(db.String(20))
    q12 = db.Column(db.String(20))
    q13 = db.Column(db.String(20))
    q14 = db.Column(db.String(20))
    q15 = db.Column(db.String(20))

    def __init__(self, gender, q1, q2,q3="",q4="",q5="",q6="",q7="",q8="",q9="",q10="",q11="",q12="",q13="",q14="",q15=""):
        self.gender = gender
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15

class Players(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    player = db.Column(db.String(100), unique=True)
    points = db.Column(db.Integer)

    def __init__(self, player, points=""):
        self.player = player
        self.point = points
