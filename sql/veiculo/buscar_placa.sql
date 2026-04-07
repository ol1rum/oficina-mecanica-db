SELECT
    id,
    placa,
    cor,
    ano,
    marca,
    modelo,
    cliente_id
FROM veiculo WHERE placa = %s