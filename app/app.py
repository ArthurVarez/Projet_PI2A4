from flask import Flask, render_template, jsonify
from flask import request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData,Column,Integer,Table,select,String,DateTime
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Bootstrap(app)


engine = create_engine('mysql+pymysql://root:password@db/API_DB')
Session = sessionmaker(bind=engine)
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

reservation = Table(
    'Reservation',
    metadata,
    Column('id',Integer, primary_key=True),
    Column("nomUtilisateur",String),
    Column("date_debut",DateTime),
    Column("date_fin",DateTime)
    
)
ressource_reserve = Table(
    'RessourceReserve',
    metadata,
    Column('idRessource',Integer, primary_key=True),
    Column('idReservation',Integer, primary_key=True),
    Column("nbGPU",Integer),
    Column("nbmemoire",Integer)
    
)




#msqldb_uri = 'mysql+mysql://user:password@localhost:3309/adminer'
#engine = create_engine(msqldb_uri)
 

@app.route("/",methods=["GET"])

def Hello():
    
    return render_template('welcome.html')



@app.route("/Ressource/",methods=["GET","POST"])
def Ressources():
    if request.method=="GET": #Renvoie la liste des Ressources
        #ressources = Ressource()
        query = select([ressources])
        conn = engine.connect()
        result = conn.execute(query)
        results = [list(row) for row in result]
        results_dict = {'results': results}
        return jsonify(results_dict)
    elif request.method=="POST": #permet d'ajouter une Ressources(il faudra verifier que l'utilisateur est admin)
        pass

@app.route("/Ressource/<id>/", methods=["GET"])
def Ressource_ID(): #renvoie la ressource avec l'ID correspondant
    pass


@app.route("/Reservation/",methods=["GET","POST"])
def Reservation():
    if request.method=="GET": #Renvoie la liste des réservations
        pass
    elif request.method=="POST": #permet d'ajouter une Réservation (utilisateur)
        pass

@app.route("/Reservation/<id>/", methods=["GET"])
def Reservation_ID(): #renvoie la réservation avec l'ID correspondant
    pass


@app.route("/RessourceReserve/", methods=["GET"])
def RessourceReserve(): #retourne la liste de toutes les ressouces réservé de tout les temps(admin?)
    pass

@app.route("/RessourceReserve/idRessource/<idRessource>", methods=["GET"])
def RessourceReserve_idRessource(): #retourne la liste des reservations d'une ressouce spécifié
    pass

@app.route("/RessourceReserve/idReservation/<idReservation>", methods=["GET"])
def RessourceReserve_idReservation():#retourne la liste des ressource d'une réservation spécifié
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)