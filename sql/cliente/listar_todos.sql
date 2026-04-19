SELECT 
    id,
    cpf,
    data_nascimento as data_nasc,
    nome_completo as nome,
    endereco
FROM cliente
ORDER BY nome_completo ASC