#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:09:02 2020

@author: Arthur
"""

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api , Resource

flask_app = Flask(__name__)
app = Api(app=flask_app,
          title='APIs Documentation',
          description=""
          )

name_space = app.namespace('User', description='')


@name_space.route('/User')


class User(Resource):
    
    #Here we have our requests
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
@name_space.route('/')

class User2(Resource):
    def get():
        pass
    


    
name_space = app.namespace('Admin', description='')
@name_space.route('/Admin')
class Admin(Resource):
    
      #Here we have our requests
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass




"""@flask_app.route("/hello")
def Hello():
    return "<h1> Hello <h1>"
"""
    
if __name__=="__main__":
   flask_app.run(host="0.0.0.0",port = 80)

