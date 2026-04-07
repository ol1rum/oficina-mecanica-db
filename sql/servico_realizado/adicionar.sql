INSERT INTO servico_realizado(
    valor_cobrado,
    ordem_servico_id,
    servico_id,
    mecanico_id
) VALUES (%s, %s, %s, %s)
RETURNING id