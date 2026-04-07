SELECT
    id,
    descricao,
    preco_padrao as preco,
    disponivel
FROM servico WHERE disponivel = true
ORDER BY descricao ASC