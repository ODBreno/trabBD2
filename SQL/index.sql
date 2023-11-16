		CREATE INDEX index_deputados_siglaPartido_idLegislatura 
        ON deputados(siglaPartido, idLegislatura);
 
        CREATE INDEX index_deputado_orgao_id
        ON deputado_orgao(id_deputado, id_orgao);

        CREATE INDEX index_evento_deputado_id 
        ON evento_deputado(id_deputado, id_evento);
        
        CREATE INDEX index_despesas_id_deputado 
        ON despesas(id_deputado);