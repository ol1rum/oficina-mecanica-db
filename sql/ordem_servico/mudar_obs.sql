UPDATE ordem_servico SET
    observacoes = %s
WHERE id = %s
RETURNING id