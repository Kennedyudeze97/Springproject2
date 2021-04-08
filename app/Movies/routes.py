from flask import Blueprint, render_template, flash, url_for, redirect
from app.Movies import movies_bp
from app import db
from app.Movies.form import Movies, FriendsSelectForm
from app.Movies.model import MoviesList
from app.Homepage.model import Friends
import random

@movies_bp.route("/AddMovies/<int:id>", methods=['POST','GET'])
def AddMovies(id):

    current_friend = Friends.query.get_or_404(id)
    form = Movies()
    userMovies = MoviesList.query.filter_by(friendId=id).first()
    print(userMovies is None)

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

        return redirect(url_for('Home.Home'))
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
    return render_template('AddMovie.html', form= form, id=id, friend=current_friend)


@movies_bp.route('/recommend', methods=['POST','GET'])
def RecommendMovie():

    form = FriendsSelectForm()

    friends = Friends.query.all()

    friendslist = [(i.id, i.firstName) for i in friends]
    form.selectedfriends.choices = friendslist

    list = []
    if form.validate_on_submit():
        for n in form.selectedfriends.data:
            movies = MoviesList.query.filter_by(friendId=n)
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

    movies = MoviesList.query.all()
    print(type(movies))

    if len(list)>0:
        randomMovie=random.choice(list)
    else:
        randomMovie="No Movie in Pool."

    return render_template('DisplayMovies.html', movie_pool = list, movies = movies, randommovie = randomMovie, form = form)