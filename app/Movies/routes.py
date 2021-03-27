from flask import Blueprint, render_template, flash, url_for, redirect
from app.Movies import movies_bp
from app import db
from app.Movies.form import Movies
from app.Movies.model import MoviesList
from app.Homepage.model import Friends

# Route to render list of friends
@movies_bp.route('/friends', methods = ["GET"])
def FriendRender():
    # Query All friends from the database
    friends = Friends.query.all()

    return render_template('Friends.html', friends = friends)

@movies_bp.route("/AddMovies/<int:id>", methods=['POST','GET'])
def AddMovies(id):
    current_friend = Friends.query.get_or_404(id)
    form = Movies()

    if form.validate_on_submit():
        # Insert data into the database
        movies = MoviesList(
            friendId=form.friendId.data, 
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
        db.session.add(movies)
        db.session.commit()

        return redirect(url_for('movies.FriendRender'))
    return render_template('AddMovie.html', form= form, id=id, friend=current_friend)


@movies_bp.route('/recommend')
def RecommendMovie():
    movies = MoviesList.query.all()
    return render_template('DisplayMovies.html', movies = movies)