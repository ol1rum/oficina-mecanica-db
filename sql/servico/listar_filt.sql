SELECT
    id,
    descricao,
    preco_padrao as preco,
    disponivel
FROM servico WHERE disponivel = %s
ORDER BY descricao ASC