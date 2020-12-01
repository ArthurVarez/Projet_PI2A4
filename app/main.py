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
          description="Here we are defining our endpoints of the API"
          )



name_space = app.namespace('Calender', 
                           description='Requests to interact with the calender'
                           )


@name_space.route('/Calender')

# requests for the calender -> get, modify ....
class Calender(Resource):
    
    #Here we have our requests
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass




name_space = app.namespace('User', description='')


@name_space.route('/User')

# requests to manage users and login/logout


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

    
name_space = app.namespace('Admin', description='')
@name_space.route('/Admin')
class Admin(Resource):
# requests the manage admin accounts and login/logout

    
      #Here we have our requests
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass




    
if __name__=="__main__":
   app.run(debug=True)
