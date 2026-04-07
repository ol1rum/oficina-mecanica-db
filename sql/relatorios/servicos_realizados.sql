SELECT 
    sr.valor_cobrado,
    sr.data_execucao,
    os.numero_os AS OS,
    s.descricao AS servico,
    m.nome_completo AS mecanico
FROM servico_realizado sr
INNER JOIN ordem_servico os ON sr.ordem_servico_id = os.id
INNER JOIN servico s ON sr.servico_id = s.id
INNER JOIN mecanico m ON sr.mecanico_id = m.id
ORDER BY sr.data_execucao DESC, sr.valor_cobrado DESC;