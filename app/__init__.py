from flask import Flask
from .config import DevConfig

#Initializing the application
app = Flask(__name__, instance_relative_config=True)
#Setting up the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from . import views