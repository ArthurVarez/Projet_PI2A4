# Projet_PI2A4-Gestionnaire du ferme de calcul


## Introduction: 

Durant notre 4ème année a l'ESILV nous avons eu a realiser un projet combinant les savoirs des deux majeures representées dans notre groupe de projet (IOS et DIA). Ainsi etant desireux de developer nos savoirs sur les technologies qui nous etait inconnues et le manegement de projet nous nous sommes rapprochés du DVIC (DeVinci Innovation Center). L'objectif etait simple : developper un web application afin de gerer les ressources mise a disposition du ferme de calcul. 

## Technologies utilisées: 

-Python/Flask
-Docker
-JWT
-SQL

##Fonctionnement

Grace à docker, le projet est deployable sur n'importe lequel appareil, juste en ayant docker installé. En effet une image python est crée via un dockerfile et un docker-compose file permet l'interaction entre cette meme image, un image MySQL et une image adminer. En donnant precisant des scripts dans le docker compose, les tables de notre bdd sont autmomatiquement crées et remplies. 

##L'API




