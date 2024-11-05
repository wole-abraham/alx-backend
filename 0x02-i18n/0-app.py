#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """ index page """
    return render_template("index.html")
