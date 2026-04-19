SELECT
    id,
    placa,
    cor,
    ano,
    marca,
    modelo,
    cliente_id
FROM veiculo WHERE cliente_id = %s
ORDER BY marca ASC, modelo ASC, ano DESC