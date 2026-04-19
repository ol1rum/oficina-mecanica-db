SELECT
    id,
    cpf,
    nome_completo as nome,
    data_contratacao,
    data_demissao,
    salario
FROM mecanico
WHERE cpf = %s