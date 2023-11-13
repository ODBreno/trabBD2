from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, SmallInteger, String, Table, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


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


class Legislatura(Base):
    __tablename__ = 'legislatura'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='legislatura_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    datainicio = Column(Date, nullable=False)
    datafim = Column(Date, nullable=False)

    deputados = relationship('Deputados', back_populates='legislatura')


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

    evento = relationship('Evento', secondary='public.evento_orgao', back_populates='orgaos')
    deputados = relationship('Deputados', secondary='public.deputado_orgao', back_populates='orgaos')


class Deputados(Base):
    __tablename__ = 'deputados'
    __table_args__ = (
        ForeignKeyConstraint(['idlegislatura'], ['public.legislatura.id'], name='deputados_idlegislatura_fkey'),
        PrimaryKeyConstraint('id', name='deputados_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    nome = Column(Text, nullable=False)
    siglapartido = Column(Text, nullable=False)
    siglauf = Column(String(2), nullable=False)
    idlegislatura = Column(SmallInteger, nullable=False)

    legislatura = relationship('Legislatura', back_populates='deputados')
    orgaos = relationship('Orgaos', secondary='public.deputado_orgao', back_populates='deputados')
    despesas = relationship('Despesas', back_populates='deputados')


t_evento_deputado = Table(
    'evento_deputado', metadata,
    Column('id_evento', Integer, nullable=False),
    Column('id_deputado', Integer, nullable=False),
    ForeignKeyConstraint(['id_evento'], ['public.evento.id'], name='evento_deputado_id_evento_fkey'),
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


t_deputado_orgao = Table(
    'deputado_orgao', metadata,
    Column('id_deputado', Integer, nullable=False),
    Column('id_orgao', Integer, nullable=False),
    ForeignKeyConstraint(['id_deputado'], ['public.deputados.id'], name='deputado_orgao_id_deputado_fkey'),
    ForeignKeyConstraint(['id_orgao'], ['public.orgaos.id'], name='deputado_orgao_id_orgao_fkey'),
    schema='public'
)


class Despesas(Base):
    __tablename__ = 'despesas'
    __table_args__ = (
        ForeignKeyConstraint(['id_deputado'], ['public.deputados.id'], name='despesas_id_deputado_fkey'),
        PrimaryKeyConstraint('id', name='despesas_pkey'),
        {'schema': 'public'}
    )

    id = Column(Text)
    numdocumento = Column(Text, nullable=False)
    coddocumento = Column(BigInteger, nullable=False)
    tipodespesa = Column(Text, nullable=False)
    datadocumento = Column(Date, nullable=False)
    valordocumento = Column(Float(53), nullable=False)
    nomefornecedor = Column(Text, nullable=False)
    cnpjcpffornecedor = Column(Text, nullable=False)
    valorliquido = Column(Float(53), nullable=False)
    id_deputado = Column(Integer, nullable=False)

    deputados = relationship('Deputados', back_populates='despesas')
