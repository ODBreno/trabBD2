from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAO():
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/trabalho_bd2")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    
    def insert(session, obj):
        session.add(obj)

class DAODeputados():
    
    def select(session, id):
        dep = session.query(Deputados).filter(Deputados.id == id).first()
        return dep
