from app import db

# This Object will facilitate the creation of 'friends' table in db when migrations are run
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(45), nullable = False)
    secondName = db.Column(db.String(200), nullable = False)

    # Method to determine how the object will be called in default
    def __repr__(self):
        return '<Friend {}>'.format(self.firstName)