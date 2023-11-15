SELECT
    deputados.id AS deputado_id,
    deputados.nome AS deputado_nome,
    legislatura.id AS legislatura_id,
    legislatura.dataInicio AS legislatura_inicio,
    orgaos.id AS orgao_id,
    orgaos.nome AS orgao_nome,
    evento.id AS evento_id,
    evento.descricao AS evento_descricao,
    despesas.valorDocumento AS despesa_valor
FROM
    deputados
JOIN legislatura ON deputados.idLegislatura = legislatura.id
JOIN deputado_orgao ON deputados.id = deputado_orgao.id_deputado
JOIN orgaos ON deputado_orgao.id_orgao = orgaos.id
JOIN evento_deputado ON deputados.id = evento_deputado.id_deputado
JOIN evento ON evento_deputado.id_evento = evento.id
JOIN despesas ON deputados.id = despesas.id_deputado
WHERE
    deputados.siglaPartido = 'PSB'
    AND legislatura.dataInicio > '2022-01-01'
    AND evento.situacao = 'Encerrada (Final)'
ORDER BY
    deputados.id, legislatura.id, orgaos.id, evento.id;