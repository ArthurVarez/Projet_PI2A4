create database gestionnairedb;
use gestionnairedb;

SET @@global.time_zone = '+00:00';
SET @@session.time_zone = '+00:00';


CREATE TABLE IF NOT EXISTS Ressource (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    quantiteMemoire int,
    quantiteGPU int
);

CREATE TABLE IF NOT EXISTS Reservation (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idRessource int,
    nomUtilisateur varchar(20),
    date_debut datetime,
    date_fin datetime,
    nbGPU int,
    nbmemoire int
);