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
        except Exception as e:
            print(e)
            session.close()
            return 0

    def selectDep(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            dep = DAODeputados.select(session, id)
            session.commit()

            return dep
        except:

            return 0
        
    def selectOrg(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOOrgaos.select(session, id)
            session.commit()
            return org
        except:
            return 0

    def selectEvent(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            event = DAOEventos.select(session, id)
            session.commit()
            return event
        except:
            return 0

    def selectPedido(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            event = DAOPedidos.select(session, id)
            session.commit()
            return event
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
                    #     print('Deputado inserido no banco. ID: ' + id + ' Nome: ' + nome)
                    # else:
                    #     print('Deputado já existe no banco. ID: ' + id + ' Nome: ' + nome)
                i+= 1
            return 1
        except Exception as e:
                return '\nERRO: ' + repr(e)
        
    def getOrgaos(self):
        try:
            i = 1
            print('Fazendo a carga dos Orgaos no banco...')
            while i < 3:
                orgaos_json = json.loads(requests.get(f'https://dadosabertos.camara.leg.br/api/v2/orgaos?pagina={i}').text)
                if len(orgaos_json) == 0:
                    raise Exception('Returned json is empty')
                for org in orgaos_json["dados"]:
                    lista_existentes = []
                    orgObject = Orgaos(id=int(org['id']),
                                            sigla=str(org['sigla']),
                                            nome=str(org['nome']),
                                            apelido=str(org['apelido']),
                                            codtipoorgao=int(org['codTipoOrgao']),
                                            tipoorgao=str(org['tipoOrgao']),
                                            nomepublicacao=str(org['nomePublicacao']),
                                        )
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectOrg(orgObject.id)
                    id = str(orgObject.id)
                    apelido = str(orgObject.apelido)
                    #Se não existir, insere no banco
                    if not check:
                        # Consultando os membros de cada orgão
                        membros_json = json.loads(requests.get(f'https://dadosabertos.camara.leg.br/api/v2/orgaos/{org["id"]}/membros?itens=1000').text)
                        for membro in membros_json["dados"]:
                            depObject = self.manipulateDB.selectDep(membro["id"])
                            if depObject and depObject.id not in lista_existentes:
                                lista_existentes.append(depObject.id)
                                orgObject.deputados.append(depObject)
                        self.manipulateDB.insert(orgObject)
                        print('Orgão inserido no banco. ID: ' + id + ' Apelido: ' + apelido)
                    else:
                        print('Orgão já existe no banco. ID: ' + id + ' Apelido: ' + apelido)
                i+= 1
            return 1
        except Exception as e:
                return '\nERRO: ' + repr(e)


    def getEventos(self):
        try:
            i = 1
            print('Fazendo a carga dos Eventos no banco...')
            while i < 11:
                eventos_json = json.loads(
                    requests.get(f'https://dadosabertos.camara.leg.br/api/v2/eventos?dataInicio=2023-01-01&pagina={i}&itens=100&ordem=ASC&ordenarPor=dataHoraInicio').text)
                if len(eventos_json) == 0:
                    raise Exception('Returned json is empty')
                for eve in eventos_json["dados"]:
                    var = str(eve['dataHoraFim'])
                    if var == 'None':
                        var = str(eve['dataHoraInicio'])

                    eveObject = Evento(     id=int(eve['id']),
                                            datahorainicio=str(eve['dataHoraInicio']),
                                            datahorafim=var,
                                            situacao=str(eve['situacao']),
                                            descricao=str(eve['descricao']),
                                            localexterno=str(eve['localExterno']),
                                            localcamara=str(eve['localCamara']['nome']),
                                       )
                    # Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectEvent(eveObject.id)
                    id = str(eveObject.id)
                    descricao = str(eveObject.id)
                    # Se não existir, insere no banco

                    if not check:
                        orgao = (eve['orgaos'][0])
                        if orgao:
                            orgaoId = self.manipulateDB.selectOrg((orgao['id']))
                            if orgaoId:
                                eveObject.orgaos.append(orgaoId)

                        self.manipulateDB.insert(eveObject)
                        print('Evento inserido no banco. ID: ' + id + ' Apelido: ' + id)
                    else:
                        print('Evento já existe no banco. ID: ' + id + ' Apelido: ' + id)
                i += 1
            return 1
        except Exception as e:
            print(e)
            return 0

    def getLicitacao(self):
        try:
            i = 1
            print('Fazendo a carga das Licitações no banco...')
            while i < 11:
                licitacao_json = json.loads(
                    requests.get(
                        f'https://dadosabertos.camara.leg.br/arquivos/licitacoesPedidos/json/licitacoesPedidos-2023.json').text)
                if len(licitacao_json) == 0:
                    raise Exception('Returned json is empty')
                for licita in licitacao_json["dados"]:
                    licitaObj = Evento(
                                        numpedido=str(licita['numPedido']),
                                        idlicitacao=str(licita['idLicitacao']),
                                        tiporegistro=str(licita['tipoRegistro']),
                                        anopedido=str(licita['anoPedido']),
                                        datahoracadastro=str(licita['dataHoraCadastro']),
                                        idorgao=str(licita['idOrgao']),
                                        ano=str(licita['ano'])
                                       )
                    # Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectPedido(licitaObj.id)
                    idLicitacao = str(licitaObj.idlicitacao)
                    numPedido = str(licitaObj.numpedido)
                    orgao = str(licitaObj.idorgao)
                    # Se não existir, insere no banco

                    if not check:
                        if orgao:
                            orgaoId = self.manipulateDB.selectOrg((orgao['id']))
                            if orgaoId:
                                licitaObj.orgaos.append(orgaoId)

                        self.manipulateDB.insert(licitaObj)
                        print('Evento inserido no banco. ID: ' + idLicitacao + ' Apelido: ' + numPedido)
                    else:
                        print('Evento já existe no banco. ID: ' + idLicitacao + ' Apelido: ' + numPedido)
                i += 1
            return 1
        except Exception as e:
            print(e)
            return 0

