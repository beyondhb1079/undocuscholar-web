from app import db

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
        return '<Name %r, Deadline %r, Amount %r>' % self.name

class Subscription(db.Model):
    # TODO: Add this for Push Notifications
    pass

