# Projet_PI2A4-Gestionnaire du ferme de calcul


## Introduction: 

Durant notre 4ème année a l'ESILV nous avons eu a realiser un projet combinant les savoirs des deux majeures representées dans notre groupe de projet (IOS et DIA). Ainsi etant desireux de developer nos savoirs sur les technologies qui nous etait inconnues et le manegement de projet nous nous sommes rapprochés du DVIC (DeVinci Innovation Center). L'objectif etait simple : developper un web application afin de gerer les ressources mise a disposition du ferme de calcul. 

## Technologies utilisées: 

-Python/Flask
-Docker
-JWT
-SQL

## Fonctionnement

Grace à docker, le projet est deployable sur n'importe lequel appareil, juste en ayant docker installé. En effet une image python est crée via un dockerfile et un docker-compose file permet l'interaction entre cette meme image, un image MySQL et une image adminer. En donnant precisant des scripts dans le docker compose, les tables de notre bdd sont autmomatiquement crées et remplies. 

## L'API

endpoints: 

_GET /Ressource_ : return all ressources 

exemple:  { "Ressources": [ { "id": 1, "quantiteGPU": 12, "quantiteMemoire": 16 }, { "id": 2, "quantiteGPU": 24, "quantiteMemoire": 16 }, { "id": 3, "quantiteGPU": 6, "quantiteMemoire": 8 } ] }

_POST /Ressource_: create a Ressource exemple of the json to post

exemple: { "id": 16, "quantiteMemoire": 12, "quantiteGPU": 15 } id value must be unique or ressource will not be add in database

_GET /Ressource/int:id_: return the Ressource with the id value 

exemple: GET /Ressource/5 return { "id": 5, "quantiteGPU": 12, "quantiteMemoire": 8 }

_GET /Reservation_: return all Reservation  
exemple: { "Reservations": [ { "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 1, "nomUtilisateur": "Remi" }, { "date_debut": "Fri, 07 Feb 2020 15:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 2, "nomUtilisateur": "Arthur" } ] }

_POST /Reservation_: create a reservation

exemple: 

{ 

  "date_debut": "2020-02-07 17:00:00",
  
  "date_fin": "2020-02-09 23:00:00" 
  
}


_GET /Reservation/int:id_ return the Reservation with this id value exemple: GET /Reservation/1 
return:  \
{ "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 1, "nomUtilisateur": "Remi" }

_GET /RessourceReserve_: return all Reserved Ressource

_POST /RessourceReserve_: Create a RessourceReservation
exemple: 

{
    "idReservation": 1, 
    "idRessource": 7, 
    "nbGPU": 7, 
    "nbMemoire": 3
}


## Base de donnees:

La table ressource a pour but de lister les ressource matériel (différente machine par exemples)
La table réservation permet de gerer les créneaux de reservation demandée par les utilisateurs tandis que la table ressource réservée permet de lister les attributions de ressource et quantité de celle-ci dédié a chaque réservation. 

![alt text](https://github.com/ArthurVarez/Projet_PI2A4/blob/master/modeleBDD/BDDV1.png)




