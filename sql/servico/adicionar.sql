INSERT INTO servico (
    descricao,
    preco_padrao
) VALUES (%s, %s)
RETURNING id