from flask import render_template
from app import app
from .request import get_movies,get_movie,search_movie


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
    movie = get_movie(movie_id)
    return render_template('movie.html',movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    return render_template('search.html',movies = searched_movies)