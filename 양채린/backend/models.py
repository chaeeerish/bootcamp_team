from db_connect import db
from datetime import datetime

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    image1 = db.Column(db.BLOB)
    image2 = db.Column(db.BLOB)
    result1 = db.Column(db.TEXT)
    result2 = db.Column(db.TEXT)