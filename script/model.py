# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError

from DAO import *
from mapeamento import *

import json
import requests
from datetime import datetime

class AcessDB:
    def insert(obj):
        try:
            session = DAO.getSession()
            DAO.insert(session, obj)
            session.commit()
            session.close()
            return 1
        except:
            return 0

    def selectDeputados(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            plat = DAODeputados.select(session, id)
            session.commit()
            session.close()
            return plat
        except:
            return 0
    
class API:
    def __init__(self):
        self.manipulateDB = AcessDB

    def getDeputados(self):
        try:
            return requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?pagina=2')
        except Exception as e:
            return '\nERRO: ' + repr(e)
