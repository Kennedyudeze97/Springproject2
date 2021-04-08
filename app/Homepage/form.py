from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.Homepage.model import Friends

class FriendsInput(FlaskForm):
    firstName = StringField("Enter First Name", validators=[DataRequired()])
    secondName = StringField("Enter Second Name", validators=[DataRequired()])
    submit = SubmitField('Submit')
