SELECT
    id,
    placa,
    cor,
    ano,
    marca,
    modelo,
    cliente_id
FROM veiculo
ORDER BY marca ASC, modelo ASC, ano DESC