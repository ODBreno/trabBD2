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

    def selectDep(id):
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
            i = 1
            print('Fazendo a carga dos Deputados no banco...')
            while i < 4:
                deputados_json = json.loads(requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=57&idLegislatura=56&idLegislatura=55&idLegislatura=54&idLegislatura=53&idLegislatura=52&idLegislatura=51&idLegislatura=50&pagina={i}').text)
                if len(deputados_json) == 0:
                    raise Exception('Returned json is empty')

                

                for dep in deputados_json["dados"]:
                    depObject = Deputados(id=int(dep['id']),
                                            nome=str(dep['nome']),
                                            siglapartido=str(dep['siglaPartido']),
                                            siglauf=str(dep['siglaUf']),
                                            idlegislatura=dep['idLegislatura'],
                                        )
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectDep(depObject.id)
                    id = str(depObject.id)
                    nome = str(depObject.nome)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(depObject)
                        print('Deputado inserido no banco. ID: ' + id + ' Nome: ' + nome)
                    else:
                        print('Deputado já existe no banco. ID: ' + id + ' Nome: ' + nome)
                i+= 1
            return 1
        except Exception as e:
                return '\nERRO: ' + repr(e)
