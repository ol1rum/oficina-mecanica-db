INSERT INTO veiculo (
    placa,
    cor,
    ano,
    marca,
    modelo,
    cliente_id
) VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id