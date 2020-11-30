#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:09:02 2020

@author: Arthur
"""

from flask import Flask
from flask import request,jsonify
import flask_swagger_ui

app = Flask(__name__)
app.config["DEBUG"] = True

#

@app.route('/')
def Test():
    return "<h1>This is a test<h1>"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)

