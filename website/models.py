from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    date = db.Column(db.Date, default=func.Date.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mins = db.relationship('Minute')
    def __repr__(self):
        return '<Meet %r>' % self.id
class Minute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dates = db.Column(db.String(10))
    topic = db.Column(db.String(10))
    attendees = db.Column(db.String(10))
    raised_by = db.Column(db.String(10))
    action = db.Column(db.String(10))
    to_be_actionedby = db.Column(db.String(10))
    info = db.Column(db.String(10))
    date_of_comp = db.Column(db.String(10))
    
   
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    meetings_id = db.Column(db.Integer, db.ForeignKey('meeting.id'))
    def __repr__(self):
        return '<Min %r>' % self.id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    minutes = db.relationship('Minute')
    meetings = db.relationship('Meeting')
   
    