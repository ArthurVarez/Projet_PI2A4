from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer,String,DateTime
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:password@localhost:3306/API_DB')
Session = sessionmaker(bind=engine,future=True)
Base= declarative_base()

class Reservation(Base):
    __tablename__ = 'Reservation'

    id = Column(Integer, primary_key=True)
    nomUtilisateur = Column(String(20))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)

class Ressource(Base):
    __tablename__ = 'Ressource'

    id = Column(Integer, primary_key=True)
    quantiteMemoire = Column(Integer)
    quantiteGPU = Column(Integer)

class RessourceReserve(Base):
    __tablename__ = 'RessourceReserve'

    idRessource = Column(Integer, primary_key=True)
    idReservation = Column(Integer, primary_key=True)
    nbGPU = Column(Integer)
    nbmemoire = Column(Integer)







@app.route("/")

def hello():
    return '<h1> Hello <h1>'




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)