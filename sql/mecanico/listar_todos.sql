SELECT
    id,
    cpf,
    nome_completo as nome,
    data_contratacao,
    data_demissao,
    salario
FROM mecanico WHERE data_demissao IS NULL
ORDER BY nome_completo ASC