from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://user:password@0.0.0.0/adminer')    
connnect = engine.connect()



@app.route("/")

def hello():
    return '<h1> Hello <h1>'

@appr.route()


if __name__ == '__main__':
    app.run(host=0.0.0.0,port=5000, debug=True)