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

GET /Ressource : return all ressources 

exemple: { "Ressources": [ { "id": 1, "quantiteGPU": 12, "quantiteMemoire": 16 }, { "id": 2, "quantiteGPU": 24, "quantiteMemoire": 16 }, { "id": 3, "quantiteGPU": 6, "quantiteMemoire": 8 } ] }

POST /Ressource: create a Ressource exemple of the json to post

exemple: { "id": 16, "quantiteMemoire": 12, "quantiteGPU": 15 } id value must be unique or ressource will not be add in database

<u>GET /Ressource/int:id </u>: return the Ressource with the id value 

exemple: GET /Ressource/5 return { "id": 5, "quantiteGPU": 12, "quantiteMemoire": 8 }

GET /Reservation: return all Reservation 

exemple: { "Reservations": [ { "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 1, "nomUtilisateur": "Remi" }, { "date_debut": "Fri, 07 Feb 2020 15:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 2, "nomUtilisateur": "Arthur" } ] }

GET /Reservation/int:id return the Reservation with this id value exemple: GET /Reservation/1 
return: { "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", "id": 1, "nomUtilisateur": "Remi" }

GET /RessourceReserve: return all Reserved Ressource




