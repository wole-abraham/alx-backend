#!/usr/bin/python3
""" Flask babel setup """
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """ Configuration for babel  """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
