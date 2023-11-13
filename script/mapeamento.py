from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, SmallInteger, String, Table, Text
from sqlalchemy.orm import declarative_base, relationship

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


class Evento(Base):
    __tablename__ = 'evento'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='evento_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    datahorainicio = Column(DateTime, nullable=False)
    situacao = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)
    datahorafim = Column(DateTime)
    localexterno = Column(Text)
    localcamara = Column(Text)

    orgaos = relationship('Orgaos', secondary='public.evento_orgao', back_populates='evento')


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
    evento = relationship('Evento', secondary='public.evento_orgao', back_populates='orgaos')
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
    Column('id_orgao', Integer, nullable=False),
    ForeignKeyConstraint(['id_evento'], ['public.evento.id'], name='evento_orgao_id_evento_fkey'),
    ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='evento_orgao_id_orgao_fkey'),
    schema='public'
)


class PedidoLicitacao(Base):
    __tablename__ = 'pedido_licitacao'
    __table_args__ = (
        ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='pedido_licitacao_id_orgao_fkey'),
        PrimaryKeyConstraint('numpedido', name='pedido_licitacao_pkey'),
        {'schema': 'public'}
    )

    numpedido = Column(Integer)
    ano = Column(SmallInteger, nullable=False)
    id_licitacao = Column(Integer, nullable=False)
    id_orgao = Column(Integer, nullable=False)
    tiporegistro = Column(Text, nullable=False)
    anopedido = Column(SmallInteger, nullable=False)
    datahoracadastro = Column(DateTime, nullable=False)

    orgaos = relationship('Orgaos', back_populates='pedido_licitacao')