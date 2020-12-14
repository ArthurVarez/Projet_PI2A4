use gestionnairedb;

INSERT INTO Ressource (id,quantiteMemoire,quantiteGPU)
 VALUES 
 (01, 16, 12),
 (02, 16, 24),
 (03, 8, 6),
 (04, 8, 6),
 (05, 8, 12),
 (06, 4, 6),
 (07, 8, 12);

INSERT INTO Reservation (id,idRessource,nomUtilisateur,date_debut,date_fin,nbGPU,nbmemoire)
 VALUES
 (01, 01, 'U001', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 2, 3),
 (02, 01, 'U002', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 1, 4),
 (03, 03, 'U003', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 2, 1),
 (04, 01, 'U004', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 2, 4),
 (05, 01, 'U005', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 1, 3),
 (06, 01, 'U006', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 1, 4),
 (07, 08, 'U007', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 1, 4),
 (08, 05, 'U008', '2010-04-05 13:43:00', '2010-04-05 15:00:00', 3, 2);

 