INSERT INTO Ressource (id,quantiteMemoire,quantiteGPU)
 VALUES 
 (01, 16, 12),
 (02, 16, 24),
 (03, 8, 6),
 (04, 8, 6),
 (05, 8, 12),
 (06, 4, 6),
 (07, 8, 12);

INSERT INTO Reservation(id, nomUtilisateur,date_debut,date_fin)
 VALUES
 (1,'Remi','2020-02-07 13:00:00','2020-02-07 17:00:00'),
 (2,'Arthur','2020-02-07 15:00:00','2020-02-07 17:00:00');


INSERT INTO RessourceReserve(idRessource, idReservation,nbGPU,nbmemoire)
 VALUES
 (1,1,12,16),
 (3,1,6,8),
 (6,2,5,2);