from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the root and its data
    '''
    popular_movies = get_movies('popular')
    return render_template('index.html', popular=popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)