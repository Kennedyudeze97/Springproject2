from app import db

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(45), nullable = False)
    secondName = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Friend {}>'.format(self.firstName)