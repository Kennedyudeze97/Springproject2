from app import db

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(45))
    secondName = db.Column(db.String(200))

    def __repr__(self):
        return '<Friend {}>'.format(self.firstName)