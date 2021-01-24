# Projet_PI2A4

Git repo for this project 


GET /Ressource : return all ressources
exemple:
{
  "Ressources": [
    {
      "id": 1, 
      "quantiteGPU": 12, 
      "quantiteMemoire": 16
    }, 
    {
      "id": 2, 
      "quantiteGPU": 24, 
      "quantiteMemoire": 16
    }, 
    {
      "id": 3, 
      "quantiteGPU": 6, 
      "quantiteMemoire": 8
    }
  ]
}

POST /Ressource: create a Ressource
exemple of the json to post:
{
    "id": 16,
    "quantiteMemoire": 12,
    "quantiteGPU": 15
}
id value must be unique or ressource will not be add in database

GET /Ressource/<int:id>: return the Ressource with the id value
exemple:
GET /Ressource/5
return
{
  "id": 5, 
  "quantiteGPU": 12, 
  "quantiteMemoire": 8
}

GET /Reservation: return all Reservation
exemple:
{
  "Reservations": [
    {
      "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", 
      "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", 
      "id": 1, 
      "nomUtilisateur": "Remi"
    }, 
    {
      "date_debut": "Fri, 07 Feb 2020 15:00:00 GMT", 
      "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", 
      "id": 2, 
      "nomUtilisateur": "Arthur"
    }
  ]
}

GET /Reservation/<int:id> return the Reservation with this id value
exemple:
GET /Reservation/1
return:
{
  "date_debut": "Fri, 07 Feb 2020 13:00:00 GMT", 
  "date_fin": "Fri, 07 Feb 2020 17:00:00 GMT", 
  "id": 1, 
  "nomUtilisateur": "Remi"
}

GET /RessourceReserve: return all Reserved Ressource 
