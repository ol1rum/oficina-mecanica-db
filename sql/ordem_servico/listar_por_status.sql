SELECT
    id,
    numero_os,
    data_hora_abertura,
    data_hora_fechamento,
    quilometragem_abertura,
    veiculo_id,
    cliente_id,
    observacoes,
    status
FROM ordem_servico WHERE status = %s
ORDER BY data_hora_abertura DESC