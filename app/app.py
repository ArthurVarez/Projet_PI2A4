from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")

def hello():
    return '<h1> Hello <h1>'

if __name__ == '__main__':
    app.run(port=5050, debug=True)