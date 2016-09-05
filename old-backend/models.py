from base_app import db
from flask_sqlalchemy import SQLAlchemy
import json

class Scholarship(db.Model):
    # TODO: Document max string lengths
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    deadline = db.Column(db.String(10))
    amount = db.Column(db.Integer)
    url = db.Column(db.String(200))

    def __init__(self, name, deadline, amount, url):
        self.name = name
        self.deadline = deadline
        self.amount = amount
        self.url = url

    def __repr__(self):
        return '%s - <Name %r, Deadline %r, Amount %r>' % (self.id, self.name, self.deadline, self.amount)
        
    def full_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
    def short_dict(self):
        return {c: getattr(self, c) for c in ['id', 'name', 'deadline', 'amount', 'url']}

# class Subscription(db.Model):
#     # TODO: Add this for Push Notifications
#     pass

