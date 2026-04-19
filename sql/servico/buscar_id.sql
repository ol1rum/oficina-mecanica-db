SELECT 
    id,
    descricao,
    preco_padrao AS preco,
    disponivel
FROM servico 
WHERE id = %s;