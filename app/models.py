from app import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))

