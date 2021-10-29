from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the root and its data
    '''
    message = "Hello world from me to you"
    return render_template('index.html', message=message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)