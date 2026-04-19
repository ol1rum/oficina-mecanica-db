SELECT
    id,
    valor_cobrado,
    data_execucao,
    ordem_servico_id as os_id,
    servico_id,
    mecanico_id
FROM servico_realizado WHERE ordem_servico_id = %s
ORDER BY data_execucao DESC