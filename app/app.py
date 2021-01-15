from flask import Flask, render_template,request,jsonify

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, MetaData,Column,Integer,Table,select,String,DateTime
from sqlalchemy.orm import sessionmaker
from config import ressources,reservation,ressource_reserve


app = Flask(__name__)
Bootstrap(app)


engine = create_engine('mysql+pymysql://root:password@db/API_DB')
Session = sessionmaker(bind=engine)


#metadata.create_all(engine)



@app.route("/",methods=["GET"])

def Hello():
    
    return render_template('welcome.html')



@app.route("/Ressource/",methods=["GET","POST"])
def Ressources():
    if request.method=="GET": #Renvoie la liste des Ressources
        #ressources = Ressource()
        query = select([ressources])
        conn = engine.connect()
        res = conn.execute(query)
        result= []
        for row in res:
            result.append({
                'id':row[0],
                'quantiteMemoire':row[1],
                'quantiteGPU':row[2]
            }
            )
        result_dict = {'Ressources': result}
        return jsonify(result_dict)
 
        
    elif request.method=="POST": #permet d'ajouter une Ressources(il faudra verifier que l'utilisateur est admin)
        pass

@app.route("/Ressource/<int:id>/", methods=["GET"])
def Ressource_ID(id): #renvoie la ressource avec l'ID correspondant
    query = select([ressources]).where(ressources.c.id==id)
    conn = engine.connect()
    res = conn.execute(query)
    results=[]
    for element in res:
        results=list(element)
    return jsonify(
        id= results[0],
        quantiteMemoire=results[1],
        quantiteGPU=results[2]
    )


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