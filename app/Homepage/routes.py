from flask import Blueprint, render_template, flash, redirect, url_for
from app.Homepage import home_bp
from app.Homepage.model import Friends
from app.Homepage.form import FriendsInput
from app import db

# This Route is the Main Route for our homepage.
@home_bp.route('/', methods = ['POST', 'GET'])
def Home():
    # Query all friends in the database
    friends = Friends.query.all()
    # Call the form instance
    form = FriendsInput()

    if form.validate_on_submit():
        data = Friends(firstName = form.firstName.data, secondName = form.secondName.data)
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('Home.Home'))
    return render_template('index.html', friends = friends, form = form)
