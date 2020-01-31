from flask import Flask
from .config import DevConfig 

#Initializing news_highlight
app =   Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)

from app import views