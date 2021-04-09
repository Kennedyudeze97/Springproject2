from flask import Blueprint, render_template, flash, redirect, url_for
from app.Homepage import home_bp
from app.Homepage.model import Friends
from app.Movies.model import MoviesList
from app.Homepage.form import FriendsInput
from app import db

# This Route is the Main Route for our homepage.
@home_bp.route('/', methods = ['POST', 'GET'])
def Home():
    # Query all friends in the database
    friends = Friends.query.all()

    # Call the form instance
    form = FriendsInput()

    # Error list
    errors = []

    # On validation, insert POST details into database and commit
    if form.validate_on_submit():
        if ((Friends.query.filter_by(firstName=form.firstName.data).first()) and Friends.query.filter_by(secondName=form.secondName.data).first()):
            errors.append("Friend already exists.")
            return render_template('index.html', friends=friends, form=form, errors=errors)
        data = Friends(firstName = form.firstName.data, secondName = form.secondName.data)
        db.session.add(data)
        db.session.commit()
        errors.append(form.firstName.data+"'s record added successfully.")

        # Run the route to the homepage
        form = FriendsInput()
        friends = Friends.query.all()
        return render_template('index.html', friends = friends, form = form, errors=errors)

    # Return index.html which is the homepage
    return render_template('index.html', friends = friends, form = form)

@home_bp.route('/delete/<int:_id>')
def delete(_id):
    deleted_user = Friends.query.filter_by(id=_id).first()
    name = deleted_user.firstName
    db.session.delete(deleted_user)
    if MoviesList.query.filter_by(friendId=_id).first():
        deleted_movielist = MoviesList.query.filter_by(friendId=_id).first()
        db.session.delete(deleted_movielist)
    db.session.commit()

    messages = []
    messages.append(name+'\'s record has been deleted successfully')

    # Query all friends in the database
    friends = Friends.query.all()

    # Call the form instance
    form = FriendsInput()

    return redirect(url_for('Home.Home'))
