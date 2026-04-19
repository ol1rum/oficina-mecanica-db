SELECT 
    id,
    valor_cobrado,
    data_execucao,
    ordem_servico_id AS os_id,
    servico_id,
    mecanico_id
FROM servico_realizado 
WHERE id = %s;