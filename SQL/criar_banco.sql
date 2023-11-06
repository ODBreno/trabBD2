-- TODO: users, indices --

-- TABELAS --

CREATE TABLE deputados (
	id int PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	siglaPartido text NOT NULL,
	siglaUf varchar(2) NOT NULL,
	idLegislatura smallint NOT NULL
)

CREATE TABLE orgaos (
	id int PRIMARY KEY NOT NULL,
	sigla text NOT NULL,
	nome text NOT NULL,	
	apelido text NOT NULL,
	codtipoOrgao smallint NOT NULL,
	tipoOrgao text NOT NULL,
	nomePublicacao text NOT NULL
)

CREATE TYPE camara as(
    nome text,
    predio text,
    sala text,
    andar text
);


CREATE TABLE eventos (
	id int PRIMARY KEY NOT NULL,
	dataHoraInicio timestamp NOT NULL,
	dataHoraFim timestamp,
	situacao text NOT NULL,	
	descricaoTipo text NOT NULL,
	descricao text NOT NULL,
	localExterno text,
	localCamara camara,
	nomePublicacao text NOT NULL
)

CREATE TABLE licitacao (
	idLicitacao int PRIMARY KEY NOT NULL,
	numero smallint NOT NULL,
	ano smallint NOT NULL,
	numProcesso int NOT NULL,
	anoProcesso smallint NOT NULL,	
	objeto text NOT NULL,
	modalidade text NOT NULL,
	tipo text NOT NULL,
	situacao text NOT NULL,
	vlrEstimado int NOT NULL,
	vlrContratado int NOT NULL,
	vlrPago int NOT NULL,
	dataAutorizacao date NOT NULL,
	dataPublicacao date NOT NULL,
	dataAbertura date NOT NULL,
	numItens int NOT NULL,
	numUnidades int NOT NULL,
	numPropostas int NOT NULL,
	numContratos int NOT NULL
)

CREATE TABLE pedido_licitacao(
	numPedido int PRIMARY KEY NOT NULL,
	ano smallint NOT NULL,
    id_licitacao int NOT NULL, 
    id_orgao smallint NOT NULL,
	tipoRegistro text NOT NULL,
	anoPedido smallint NOT NULL,
	dataHoraCadastro timestamp NOT NULL,
	observacoes text NOT NULL,
    FOREIGN KEY (id_licitacao) REFERENCES licitacao(idLicitacao),
    FOREIGN KEY (id_orgao) REFERENCES orgaos(id)
);

-- RELAÇÕES --

CREATE TABLE deputado_orgao(
    id_deputado int NOT NULL, 
    id_orgao smallint NOT NULL,
    FOREIGN KEY (id_deputado) REFERENCES deputados(id),
    FOREIGN KEY (id_orgao) REFERENCES orgaos(id)
);

