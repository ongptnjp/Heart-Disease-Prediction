#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:18:02 2020

@author: tanatjakphan
"""

import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "<body><h2>Hello World!</h2></body"

@app.route("/greet/<name>")
def greet(name):
    return "<body><h2>Hello {}!</h2></body>".format(name)

if __name__ == "__main__":
    app.run(debug = True)
