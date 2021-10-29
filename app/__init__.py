from flask import Flask
from .config import DevConfig

#Initializing the application
app = Flask(__name__)
#Setting up the configuration
app.config.from_object(DevConfig)

from . import views