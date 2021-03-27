from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# flask Form on the ten friend's movies
class Movies(FlaskForm):
    friendId = StringField('Enter Friend Id')
    movie1 = StringField('Enter Movie-1')
    movie2 = StringField('Enter Movie-2')
    movie3 = StringField('Enter Movie-3')
    movie4 = StringField('Enter Movie-4')
    movie5 = StringField('Enter Movie-5')
    movie6 = StringField('Enter Movie-6')
    movie7 = StringField('Enter Movie-7')
    movie8 = StringField('Enter Movie-8')
    movie9 = StringField('Enter Movie-9')
    movie10 = StringField('Enter Movie-10')
    submit = SubmitField('Enter')