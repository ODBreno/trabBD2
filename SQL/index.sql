	-- Índices para a tabela deputados
CREATE INDEX index_deputados_siglaPartido_idLegislatura ON deputados(siglaPartido, idLegislatura);

-- Índices para a tabela legislatura
CREATE INDEX index_legislatura_dataInicio ON legislatura(dataInicio);

-- Índices para a tabela deputado_orgao
CREATE INDEX index_deputado_orgao_id_deputado ON deputado_orgao(id_deputado);
CREATE INDEX index_deputado_orgao_id_orgao ON deputado_orgao(id_orgao);

-- Índices para a tabela orgaos
CREATE INDEX index_orgaos_id ON orgaos(id);

-- Índices para a tabela evento_deputado
CREATE INDEX index_evento_deputado_id_deputado ON evento_deputado(id_deputado);
CREATE INDEX index_evento_deputado_id_evento ON evento_deputado(id_evento);

-- Índices para a tabela evento
CREATE INDEX index_evento_id ON evento(id);

-- Índices para a tabela despesas
CREATE INDEX index_despesas_id_deputado ON despesas(id_deputado);