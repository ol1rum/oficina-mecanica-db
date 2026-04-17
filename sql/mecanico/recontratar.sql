UPDATE mecanico SET 
    nome_completo = %s,
    data_contratacao = %s,
    data_demissao = NULL,
    salario = %s
WHERE cpf = %s
RETURNING id