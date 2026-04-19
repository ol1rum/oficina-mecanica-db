UPDATE ordem_servico SET
    data_hora_fechamento = CURRENT_TIMESTAMP,
    status = %s
where id = %s
RETURNING id