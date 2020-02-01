from flask import Flask
from .config import DevConfig 
from flask_bootsrap import Bootstrap


#Initializing news_highlight
app =   Flask(__name__,instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask extensions
bootsrap = Bootstrap(app)


from app import views
from app import error