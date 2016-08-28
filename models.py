from app import db

class Scholarship(db.Model):
    # TODO: Document max string lengths
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    deadline = db.Column(db.String(10))
    amount = db.Column(db.Integer)
    website = db.Column(db.String(200))

    def __init__(self, name, deadline, amount, website):
        self.name = name
        self.deadline = deadline
        self.amount = amount
        self.website = website

    def __repr__(self):
        return '<Name %r, Deadline %r, Amount %r>' % self.name

class Subscription(db.Model):
    # TODO: Add this for Push Notifications
    pass

