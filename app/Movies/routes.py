from flask import Blueprint, render_template, flash, url_for, redirect
from app.Movies import movies_bp
from app import db
from app.Movies.form import Movies, FriendsSelectForm
from app.Movies.model import MoviesList
from app.Homepage.model import Friends
import random

# Route to the page that enables modifying of friend's movie list
@movies_bp.route("/AddMovies/<int:id>", methods=['POST','GET'])
def AddMovies(id):
    # Get friend from the database
    current_friend = Friends.query.get_or_404(id)
    form = Movies()
    # Get the movies of the friend selected
    userMovies = MoviesList.query.filter_by(friendId=id).first()

    # If a form is POSTED, it is validated and then movies data obtained
    if form.validate_on_submit():
        # Insert data into the database
        movies = MoviesList(
            friendId = id,
            movie1 = form.movie1.data,
            movie2 = form.movie2.data,
            movie3 = form.movie3.data,
            movie4 = form.movie4.data,
            movie5 = form.movie5.data,
            movie6 = form.movie6.data,
            movie7 = form.movie7.data,
            movie8 = form.movie8.data,
            movie9 = form.movie9.data,
            movie10 = form.movie10.data)

        # Check if the friend has movies list. if not, add movies to list. if so, modify(Update) current movies
        if userMovies is None:
            db.session.add(movies)
        else:
            userMovies.movie1 = form.movie1.data
            userMovies.movie2 = form.movie2.data
            userMovies.movie3 = form.movie3.data
            userMovies.movie4 = form.movie4.data
            userMovies.movie5 = form.movie5.data
            userMovies.movie6 = form.movie6.data
            userMovies.movie7 = form.movie7.data
            userMovies.movie8 = form.movie8.data
            userMovies.movie9 = form.movie9.data
            userMovies.movie10 = form.movie10.data
        db.session.commit()

        # Go back to homepage
        return redirect(url_for('Home.Home'))

    # Create form. if friend has a movie list, populate form with necessary data
    if userMovies is None:
        form = Movies()
    else:
        form.movie1.data = userMovies.movie1
        form.movie2.data = userMovies.movie2
        form.movie3.data = userMovies.movie3
        form.movie4.data = userMovies.movie4
        form.movie5.data = userMovies.movie5
        form.movie6.data = userMovies.movie6
        form.movie7.data = userMovies.movie7
        form.movie8.data = userMovies.movie8
        form.movie9.data = userMovies.movie9
        form.movie10.data = userMovies.movie10

    # Return the html page to modify user's movies list
    return render_template('AddMovie.html', form= form, id=id, friend=current_friend)

# Route to the Movie recommendation page
@movies_bp.route('/recommend', methods=['POST','GET'])
def RecommendMovie():
    # Create the form object for the selection of participating friends
    form = FriendsSelectForm()
    # Query db for a list of all friends
    friends = Friends.query.all()
    # Create a set of friend's details to be used in the friend's selection form
    friendslist = [(i.id, i.firstName) for i in friends]
    form.selectedfriends.choices = friendslist
    # Create a list of movies for the movie pool
    list = []

    # Validate form of selected friends
    if form.validate_on_submit():

        # Loop through each friend selected for the movie night and obtain their movie list form db
        for n in form.selectedfriends.data:
            movies = MoviesList.query.filter_by(friendId=n)

            # Populate movies list with all the movies in the selected friend's movie list
            for m in movies:
                if m.movie1:
                    list.append(m.movie1)
                if m.movie2:
                    list.append(m.movie2)
                if m.movie3:
                    list.append(m.movie3)
                if m.movie4:
                    list.append(m.movie4)
                if m.movie5:
                    list.append(m.movie5)
                if m.movie6:
                    list.append(m.movie6)
                if m.movie7:
                    list.append(m.movie7)
                if m.movie8:
                    list.append(m.movie8)
                if m.movie9:
                    list.append(m.movie9)
                if m.movie10:
                    list.append(m.movie10)

    # Check if list has any value and return the movies as a pool. Otherwise print  No movie in pool
    if len(list)>0:
        randomMovie=random.choice(list)
    else:
        randomMovie="No Movie in Pool."

    # Render the html page for movie recommendation
    return render_template('DisplayMovies.html', movie_pool = list, randommovie = randomMovie, form = form)