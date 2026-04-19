SELECT
    os.numero_os,
    c.nome_completo as cliente_nome,
    c.cpf as cliente_cpf,
    v.placa as veiculo_placa,
    os.quilometragem_abertura,
    os.data_hora_abertura,
    os.data_hora_fechamento,
    os.status,
    os.observacoes
FROM ordem_servico os 
INNER JOIN cliente c ON os.cliente_id = c.id
INNER JOIN veiculo v ON os.veiculo_id = v.id
WHERE os.id = %s