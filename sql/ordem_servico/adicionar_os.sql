INSERT INTO ordem_servico (
    numero_os,
    quilometragem_abertura,
    veiculo_id,
    cliente_id,
    observacoes
) VALUES (%s, %s, %s, %s, %s)
RETURNING id