from flask import Flask, render_template,request,jsonify

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine,select,insert, between
from sqlalchemy.sql import and_, or_
from sqlalchemy.orm import sessionmaker
from config import *

app = Flask(__name__)
Bootstrap(app)


engine = create_engine('mysql+pymysql://root:password@db/API_DB')
Session = sessionmaker(bind=engine)



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
        if not request.json:
            return 'nojson'
        if not request.json or not 'id'in request.json or not 'quantiteMemoire' in request.json or not 'quantiteGPU' in request.json:
            return "400"
        else:
            content = request.json
            query= ressources.insert(None).values(id=content["id"], quantiteGPU=content["quantiteGPU"],quantiteMemoire=content["quantiteMemoire"])
            conn = engine.connect()
            res = conn.execute(query)
            return str(content["id"])
        

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
        query = select([reservations])
        conn = engine.connect()
        res = conn.execute(query)
        result= []
        for row in res:
            result.append({
            'id': row[0],
            'nomUtilisateur':row[1],
            'date_debut':row[2],
            'date_fin':row[3]
            })
        result_dict = {'Reservations': result}
        return jsonify(result_dict)
    elif request.method=="POST": #permet d'ajouter une Réservation (utilisateur)    
        if not request.json or not 'date_debut'in request.json or not 'date_fin' in request.json:
            return "invalid request"
        else:
            content = request.json
            query= reservations.insert(None).values(nomUtilisateur= "", date_debut = content["date_debut"],date_fin =content["date_fin"])
            conn = engine.connect()
            res = conn.execute(query)
            return "200"
        

@app.route("/Reservation/<int:id>/", methods=["GET"])
def Reservation_ID(id): #renvoie la réservation avec l'ID correspondant
        query = select([reservations]).where(reservations.c.id==id)
        conn = engine.connect()
        res = conn.execute(query)
        results=[]
        for element in res:
            results=list(element)
        return jsonify(
            id= results[0],
            nomUtilisateur=results[1],
            date_debut=results[2],
            date_fin=results[3]
        )


@app.route("/RessourceReserve/", methods=["GET","POST"])
def RessourceReserve(): #retourne la liste de toutes les ressouces réservé de tout les temps(admin?)
    if request.method=="GET":
        query = select([ressource_reserve])
        conn = engine.connect()
        res = conn.execute(query)
        result= []
        for row in res:
            result.append({
                'idRessource':row[0],
                'idReservation':row[1],
                'nbGPU':row[2],
                'nbmemoire':row[3]
            })
        result_dict = {'RessourceReserve': result}
        return jsonify(result_dict)
    elif request.method=="POST":
        if not request.json or not 'idReservation'in request.json or not 'idRessource' in request.json or not 'nbGPU' in request.json or not 'nbMemoire' in request.json:
            return "invalid json data" #on vérifie que les élément du json existe
        else:
            content=request.json
            query = select([ressources]).where(ressources.c.id==content['idRessource'])
            conn = engine.connect()
            res = conn.execute(query)
            ressourceExiste=False
            globalGPUValid = False
            globalmemoryValid = False
             #on verifie que la Ressource existe et que les demandes GPU et mémoire ne sont pas supérieur au quantité de la ressource            
            quantiteGPU=0
            quantiteMemoire=0
            for row in res:
                ressourceExiste=True
                quantiteGPU = row[2]
                quantiteMemoire= row[1]
            if content["nbGPU"]<quantiteGPU:
                globalGPUValid=True
            if content["nbMemoire"]<quantiteMemoire:
                globalmemoryValid = True
            query = select([reservations]).where(reservations.c.id==content['idReservation'])
            conn = engine.connect()
            res = conn.execute(query)
            reservationExiste=False
            currentReservation={}
            #on verifie que la Reservation existe          
            for row in res:
                reservationExiste=True
                currentReservation={
                    'id': row[0],
                    'nomUtilisateur':row[1],
                    'date_debut':row[2],
                    'date_fin':row[3]
                }
            if globalGPUValid and globalmemoryValid and ressourceExiste and reservationExiste:
                query = select([ressource_reserve, reservations]).where(
                    and_(
                        reservations.c.id == ressource_reserve.c.idReservation,
                        ressource_reserve.c.idRessource == content['idRessource'],
                        or_(
                            between(reservations.c.date_debut,currentReservation["date_debut"],currentReservation["date_fin"]),
                            between(reservations.c.date_fin,currentReservation["date_debut"],currentReservation["date_fin"]),
                            between(currentReservation["date_debut"],reservations.c.date_debut,reservations.c.date_fin)
                        )
                    )
                ).order_by('date_debut')
                conn = engine.connect()
                res= None
                res = conn.execute(query)
                currentReservationRessource=[content["nbGPU"],content["nbMemoire"]]

                tabdatenonfini=[] #on ajoute [nbGPU, nbMemoire, dateFin] 
                quantiteRessourceutilise=[0,0] # [nbGPU, nbMemoire]

                chaine=""
                for row1 in res:
                    for row2 in tabdatenonfini : 
                        # si date fin est avant datedebut de row1 on soustrait dans quantité ressource utillisé et on remove l'élément de tabdatenonfini
                        #return str(type(row2[2]))+ "  " +str(type(row1[6])) + " \n" +chaine+ str(content['idRessource']) + str(row2[2]) + str(row1[6])
                        if row2[2] < row1[6] :
                            quantiteRessourceutilise[0]-=row2[0]
                            quantiteRessourceutilise[0]-=row2[0]
                            tabdatenonfini.remove(row2)
                    #on ajoute les ressource utilisé par row1 a quantiteRessourceutilise
                    quantiteRessourceutilise[0] +=row1[2]
                    quantiteRessourceutilise[1] +=row1[3]
                    #si quantité ressource utilisé > quantité max on retourne pas possible
                    if(quantiteRessourceutilise[0]+currentReservationRessource[0]>quantiteGPU or quantiteRessourceutilise[1]+currentReservationRessource[1]>quantiteMemoire):
                        return "Request impossible dépassement ressource" +"quantitéGPU "+ str(quantiteRessourceutilise[0])+"  " + str(currentReservationRessource[0]) +" "+ str(quantiteGPU)
                    tabdatenonfini.append([row1[2],row1[3],row1[7]])
                # insertion de la ressourceReservé
                content = request.json
                query= ressource_reserve.insert(None).values(idRessource=content['idRessource'],idReservation=content['idReservation'],nbGPU=content['nbGPU'],nbmemoire=content['nbMemoire'])
                conn = engine.connect()
                res = conn.execute(query)
                return "200"
            else:
                return "invalid request"

                                

    

@app.route("/RessourceReserve/idRessource/<int:id>", methods=["GET"])
def RessourceReserve_idRessource(id): #retourne la liste des reservations d'une ressouce spécifié
    query = select([ressource_reserve]).where(ressource_reserve.c.idRessource==id)
    conn = engine.connect()
    res = conn.execute(query)
    results=[]
    for row in res:
        results.append({
            'idRessource':row[0],
            'idReservation':row[1],
            'nbGPU':row[2],
            'nbmemoire':row[3]
        })
    result_dict = {'RessourceReserve': results}
    return jsonify(result_dict)

@app.route("/RessourceReserve/idReservation/<int:id>", methods=["GET"])
def RessourceReserve_idReservation(id):#retourne la liste des ressource d'une réservation spécifié
    query = select([ressource_reserve]).where(ressource_reserve.c.idReservation==id)
    conn = engine.connect()
    res = conn.execute(query)
    results=[]
    for row in res:
        results.append({
            'idRessource':row[0],
            'idReservation':row[1],
            'nbGPU':row[2],
            'nbmemoire':row[3]
        })
    result_dict = {'RessourceReserve': results}
    return jsonify(result_dict)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)