#!/usr/bin/env python3
""" Flask babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Configuration for babel  """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get best locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ index page """
    return render_template("2-index.html")
