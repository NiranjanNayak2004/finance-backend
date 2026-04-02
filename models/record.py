from extensions import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    type = db.Column(db.String(10))
    category = db.Column(db.String(50))
    date = db.Column(db.String(20))
    notes = db.Column(db.String(200))