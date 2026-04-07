INSERT INTO mecanico (
    cpf,
    nome_completo,
    data_contratacao,
    salario
) VALUES (%s, %s, %s, %s)
RETURNING id