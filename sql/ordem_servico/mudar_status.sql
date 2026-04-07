UPDATE ordem_servico SET
    status = %s
WHERE id = %s
RETURNING id