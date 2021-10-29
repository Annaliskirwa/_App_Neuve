from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the root and its data
    '''
    return render_template('index.html')