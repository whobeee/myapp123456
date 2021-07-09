from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Binary, Column, Integer, String





class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    name1 = db.Column(db.String(150))
    website =db.Column(db.String(150))
    ipaddr =db.Column(db.String(150))

   