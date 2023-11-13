from sqlalchemy import Column, Date, DateTime, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, SmallInteger, \
    String, Table, Text, TypeDecorator, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.sqltypes import NullType, TEXT

Base = declarative_base()
metadata = Base.metadata


class Deputados(Base):
    __tablename__ = 'deputados'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='deputados_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    nome = Column(Text, nullable=False)
    siglapartido = Column(Text, nullable=False)
    siglauf = Column(String(2), nullable=False)
    idlegislatura = Column(SmallInteger, nullable=False)

    orgaos = relationship('Orgaos', secondary='public.deputado_orgao', back_populates='deputados')


class Camara(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = f"({value['nome']}, {value['predio']}, {value['sala']}, {value['andar']})"
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = eval(value)
        return value


class Evento(Base):
    __tablename__ = 'evento'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='eventos_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer, primary_key=True, nullable=False)
    dataHoraInicio = Column(DateTime, nullable=False)
    dataHoraFim = Column(DateTime)
    situacao = Column(String, nullable=False)
    descricao = Column(Text, nullable=False)
    localExterno = Column(String)
    localCamara = Column(String)

    orgaos = relationship('Orgaos', secondary='public.evento_orgao', back_populates='evento')

class Licitacao(Base):
    __tablename__ = 'licitacao'
    __table_args__ = (
        PrimaryKeyConstraint('idlicitacao', name='licitacao_pkey'),
        {'schema': 'public'}
    )

    idlicitacao = Column(Integer)
    numero = Column(SmallInteger, nullable=False)
    ano = Column(SmallInteger, nullable=False)
    numprocesso = Column(Integer, nullable=False)
    anoprocesso = Column(SmallInteger, nullable=False)
    objeto = Column(Text, nullable=False)
    modalidade = Column(Text, nullable=False)
    tipo = Column(Text, nullable=False)
    situacao = Column(Text, nullable=False)
    vlrestimado = Column(Integer, nullable=False)
    vlrcontratado = Column(Integer, nullable=False)
    vlrpago = Column(Integer, nullable=False)
    dataautorizacao = Column(Date, nullable=False)
    datapublicacao = Column(Date, nullable=False)
    dataabertura = Column(Date, nullable=False)
    numitens = Column(Integer, nullable=False)
    numunidades = Column(Integer, nullable=False)
    numpropostas = Column(Integer, nullable=False)
    numcontratos = Column(Integer, nullable=False)

    pedido_licitacao = relationship('PedidoLicitacao', back_populates='licitacao')


class Orgaos(Base):
    __tablename__ = 'orgaos'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='orgaos_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    sigla = Column(Text, nullable=False)
    nome = Column(Text, nullable=False)
    apelido = Column(Text, nullable=False)
    codtipoorgao = Column(SmallInteger, nullable=False)
    tipoorgao = Column(Text, nullable=False)
    nomepublicacao = Column(Text, nullable=False)

    deputados = relationship('Deputados', secondary='public.deputado_orgao', back_populates='orgaos')
    eventos = relationship('Evento', secondary='public.evento_orgao', back_populates='orgaos')

    pedido_licitacao = relationship('PedidoLicitacao', back_populates='orgaos')


t_deputado_orgao = Table(
    'deputado_orgao', metadata,
    Column('id_deputado', Integer, nullable=False),
    Column('id_orgao', SmallInteger, nullable=False),
    ForeignKeyConstraint(['id_deputado'], ['public.deputados.id'], name='deputado_orgao_id_deputado_fkey'),
    ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='deputado_orgao_id_orgao_fkey'),
    schema='public'
)

t_evento_orgao = Table(
    'evento_orgao', metadata,
    Column('id_evento', Integer, nullable=False),
    Column('id_orgao', SmallInteger, nullable=False),
    ForeignKeyConstraint(['id_evento'], ['public.evento.id'], name='evento_orgao_id_evento_fkey'),
    ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='evento_orgao_id_orgao_fkey'),
    schema='public'
)


class PedidoLicitacao(Base):
    __tablename__ = 'pedido_licitacao'
    __table_args__ = (
        ForeignKeyConstraint(['id_licitacao'], ['public.licitacao.idlicitacao'], name='pedido_licitacao_id_licitacao_fkey'),
        ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='pedido_licitacao_id_orgao_fkey'),
        PrimaryKeyConstraint('numpedido', name='pedido_licitacao_pkey'),
        {'schema': 'public'}
    )

    numpedido = Column(Integer)
    ano = Column(SmallInteger, nullable=False)
    id_licitacao = Column(Integer, nullable=False)
    id_orgao = Column(SmallInteger, nullable=False)
    tiporegistro = Column(Text, nullable=False)
    anopedido = Column(SmallInteger, nullable=False)
    datahoracadastro = Column(DateTime, nullable=False)
    observacoes = Column(Text, nullable=False)

    licitacao = relationship('Licitacao', back_populates='pedido_licitacao')
    orgaos = relationship('Orgaos', back_populates='pedido_licitacao')
