UPDATE ordem_servico SET
    data_hora_fechamento = %s,
    status = %s
where id = %s
RETURNING id