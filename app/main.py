#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:09:02 2020

@author: Arthur
"""

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask,request
from flask_restplus import Api , Resource
import MySQLdb

DB = MySQLdb.connect('Calender', user='root',password=None)
flask_app = Flask(__name__)
flask_app.config["DEBUG"]=True
app = Api(app=flask_app,
          title='PI24-APIs Documentation',
          description="Here we are defining our endpoints of the API"
          )



name_space = app.namespace('Calender', 
                           description='Requests to interact with the calender'
                           )



users ={}
admin = {}


@name_space.route('/Calender')

# requests for the calender -> get, modify ....
class Calender(Resource):
    
    #Here we have our requests
    def get(self):
        cur = MySQLdb.cursors()
        rep = cur.execute("SELECT * FROM YOUR_TABLE_NAME")
        return rep 
        
    def post(self):
        
        pass
    
    def put(self):
        pass
    def delete(self):
        pass




"""name_space = app.namespace('User', description='')


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
    
    
@name_space.route('/login')
class LogInUser(Resource):
    
    def get(username, password):
        return "connected",200
        
@name_space.route('/logout')
class LogOutUser(Resource):
    def get(self, username):
        return "disconnect",200
        
    
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
    
@name_space.route('/login')  
class LogInAdmin(Resource):
    
    def get(username, password):
        return "connected",200
        
@name_space.route('/logout')
class LogOutAdmin(Resource):
    def get(self, username):
        return "disconnect",200
        
"""    



    
if __name__=="__main__":
   flask_app.run(host='0.0.0.0',port=80)

