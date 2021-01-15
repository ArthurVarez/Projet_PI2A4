

SET @@global.time_zone = '+00:00';
SET @@session.time_zone = '+00:00';


CREATE TABLE IF NOT EXISTS Ressource (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    quantiteMemoire int,
    quantiteGPU int
);

CREATE TABLE IF NOT EXISTS Reservation (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomUtilisateur varchar(20),
    date_debut datetime,
    date_fin datetime
);

CREATE TABLE IF NOT EXISTS RessourceReserve (
    idRessource int,
    idReservation int,
    nbGPU int,
    nbmemoire int,
    PRIMARY KEY (idRessource,idReservation)
);
