from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer,String,DateTime, Table , MetaData
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:password@localhost:3306/API_DB')
Session = sessionmaker(bind=engine,future=True)
Base= declarative_base()
metadata= MetaData()
"""
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
    """

#metadata.create_all(engine)

ressources = Table(
    'Ressource',
    metadata,
    Column('id',Integer, primary_key=True),
    Column("quantiteMemoire",Integer),
    Column("quantiteGPU",Integer)

)




@app.route("/")

def hello():
    return '<h1> Hello <h1>'

@app.route("/Ressource",methods=["GET"])

def get_ressources():
    #ressources = Ressource()
    query = select([ressources])
    conn = engine.connect()
    res = conn.execute(query)
    chain = ""
    for element in res:
        chain = chaine + str(element)
    res.close()
    return chain

"""@app.route("/Reservation",methods=["GET"])
    def get_reservation():
        reservations = Reservation()
        pass

@app.route("/RessourceReserve")
    def get_ressourcereserve():
        pass
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)