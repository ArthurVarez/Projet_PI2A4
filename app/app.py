from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine

app = Flask(__name__)
 msqldb_uri = 'mysql+mysql://user:password@localhost:3309/adminer'
 engine = create_engine(msqldb_uri)
 



@app.route("/")

def hello():
    return '<h1> Hello <h1>'




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)