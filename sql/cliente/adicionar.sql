INSERT INTO cliente (
    cpf,
    data_nascimento,
    nome_completo,
    endereco
) VALUES (%s, %s, %s, %s)
RETURNING id