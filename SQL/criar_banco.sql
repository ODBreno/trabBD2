-- TODO:indices --

CREATE ROLE usuario;
CREATE ROLE dev;
CREATE ROLE dba;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO usuario;
GRANT SELECT, INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA public TO dev;
GRANT ALL ON DATABASE "trabalho_bd2" TO dba;

CREATE USER deputadosDBA WITH PASSWORD 'deputadosDBA';
CREATE USER deputadosDEV WITH PASSWORD 'deputadosDEV';
CREATE USER deputadosUSER WITH PASSWORD 'deputadosUSER';

GRANT usuario TO deputadosUSER;
GRANT dev TO deputadosDEV;
GRANT dba TO deputadosDBA;

GRANT USAGE ON SCHEMA public TO martinsUSER;
GRANT USAGE ON SCHEMA public TO martinsDEV;
GRANT USAGE ON SCHEMA public TO martinsDBA;


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

-- CONSULTAS --
SELECT * FROM legislatura
SELECT * FROM orgaos
SELECT * FROM despesas
SELECT * FROM evento
SELECT * FROM deputados
SELECT * FROM evento_deputado 
SELECT * FROM evento_orgao
SELECT * FROM deputado_orgao
SELECT * FROM deputados join legislatura on deputados.idlegislatura = legislatura.id

DELETE FROM deputados
DELETE FROM despesas

CREATE OR REPLACE FUNCTION count_rows(tablename text) 
    RETURNS integer AS
    	$$
    	DECLARE
    		result integer;
    	BEGIN
    		EXECUTE 'SELECT count(*) FROM ' || 
                tablename INTO result;
    		RETURN result;
    	END;
        $$ language plpgsql;

SELECT table_name, count_rows(table_name) 
FROM information_schema.tables 
WHERE table_schema NOT IN 
	('pg_catalog', 'information_schema') 
ORDER by count_rows(table_name) DESC


