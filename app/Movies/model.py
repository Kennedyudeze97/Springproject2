from app import db

# Class to create movies_list table the database on movies to be entered by a friend
class MoviesList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    friendId = db.Column(db.Integer, db.ForeignKey('friends.id'))
    movie1 = db.Column(db.String(64))
    movie2 = db.Column(db.String(64))
    movie3 = db.Column(db.String(64))
    movie4 = db.Column(db.String(64))
    movie5 = db.Column(db.String(64))
    movie6 = db.Column(db.String(64))
    movie7 = db.Column(db.String(64))
    movie8 = db.Column(db.String(64))
    movie9 = db.Column(db.String(64))
    movie10 = db.Column(db.String(64))

    # Function that specifies how the object is named
    def __repr__(self):
        return '<Movie {}>'.format(self.movie1)