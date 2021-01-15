
from sqlalchemy import create_engine, MetaData,Column,Integer,Table,select,String,DateTime


metadata= MetaData()

ressources = Table(
    'Ressource',
    metadata,
    Column('id',Integer, primary_key=True),
    Column("quantiteMemoire",Integer),
    Column("quantiteGPU",Integer)

)

reservations = Table(
    'Reservation',
    metadata,
    Column('id',Integer, primary_key=True),
    Column("nomUtilisateur",String),
    Column("date_debut",DateTime),
    Column("date_fin",DateTime)
    
)
ressource_reserve = Table(
    'RessourceReserve',
    metadata,
    Column('idRessource',Integer, primary_key=True),
    Column('idReservation',Integer, primary_key=True),
    Column("nbGPU",Integer),
    Column("nbmemoire",Integer)
    
)