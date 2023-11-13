-- TODO: users, indices --

-- TABELAS --
CREATE TABLE legislatura (
	id int PRIMARY KEY NOT NULL,
	dataInicio date NOT NULL,
	dataFim date NOT NULL
)

CREATE TABLE deputados (
	id int PRIMARY KEY NOT NULL,
	nome text NOT NULL,
	siglaPartido text NOT NULL,
	siglaUf varchar(2) NOT NULL,
	idLegislatura smallint NOT NULL,
	FOREIGN KEY (idLegislatura) REFERENCES legislatura(id)
)

CREATE TABLE despesas (
	id text PRIMARY KEY NOT NULL,
	numDocumento text NOT NULL,
	codDocumento bigint NOT NULL,
	tipoDespesa text NOT NULL,
	dataDocumento date NOT NULL,	
	valorDocumento float NOT NULL,
	nomeFornecedor text NOT NULL,
	cnpjCpfFornecedor text NOT NULL,
	valorLiquido float NOT NULL,
	id_deputado int NOT NULL,
	FOREIGN KEY (id_deputado) REFERENCES deputados(id)
)

CREATE TABLE orgaos (
	id int PRIMARY KEY NOT NULL,
	sigla text NOT NULL,
	nome text NOT NULL,	
	apelido text NOT NULL,
	codtipoOrgao int NOT NULL,
	tipoOrgao text NOT NULL,
	nomePublicacao text NOT NULL
)

CREATE TABLE evento (
	id int PRIMARY KEY NOT NULL,
	dataHoraInicio timestamp NOT NULL,
	dataHoraFim timestamp NULL,
	situacao text NOT NULL,
	descricao text NOT NULL,
	localExterno text,
	localCamara text
)

CREATE TABLE deputado_orgao(
    id_deputado int NOT NULL, 
    id_orgao int NOT NULL,
    FOREIGN KEY (id_deputado) REFERENCES deputados(id),
    FOREIGN KEY (id_orgao) REFERENCES orgaos(id)
);

CREATE TABLE evento_orgao(
    id_evento int NOT NULL,
    id_orgao int NOT NULL,
    FOREIGN KEY (id_evento) REFERENCES evento(id),
    FOREIGN KEY (id_orgao) REFERENCES orgaos(id)
)

CREATE TABLE evento_deputado(
    id_evento int NOT NULL,
    id_deputado int NOT NULL,
    FOREIGN KEY (id_evento) REFERENCES evento(id),
    FOREIGN KEY (id_deputado) REFERENCES deputados(id)
)


SELECT * FROM legislatura
SELECT * FROM orgaos
SELECT * FROM despesas
SELECT * FROM evento
SELECT * FROM evento_deputado 
SELECT * FROM deputados join legislatura on deputados.idlegislatura = legislatura.id

DELETE FROM deputados
DELETE FROM despesas


