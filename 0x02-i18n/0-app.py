#!/usr/bin/env python3
""" basic flask application 0x02-i18n """
from flask import Flask, render_template
from typing import Text

app = Flask(__name__)


@app.route("/")
def index() -> Text:
    """ index page """
    return render_template("index.html")
