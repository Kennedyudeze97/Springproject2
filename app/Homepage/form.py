# Import necessary modules for creation of form objects
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired

# This form, when rendered in html, enables insertion of a new friend's details
class FriendsInput(FlaskForm):
    firstName = StringField("Enter First Name", validators=[DataRequired()])
    secondName = StringField("Enter Second Name", validators=[DataRequired()])
    submit = SubmitField('Submit')
