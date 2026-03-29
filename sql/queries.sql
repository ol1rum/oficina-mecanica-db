-- SELECT * FROM cliente;
-- SELECT * FROM veiculo;
-- SELECT * FROM telefone;
-- SELECT * FROM ordem_servico;
-- SELECT * FROM servico;
-- SELECT * FROM mecanico;

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

-- CUSTO TOTAL COM MECANICOS
SELECT
    COUNT(m.id) AS total_mecanico,
    SUM(m.salario) AS custo_total,
    AVG(m.salario) AS media_salario
FROM mecanico m;

-- CONTAGEM DE RECEITA
SELECT 
    SUM(sr.valor_cobrado) AS receita_total,
    AVG(sr.valor_cobrado) AS ticket_medio
FROM servico_realizado sr;

-- RANKING SERVICOS MAIS PROCURADOS
SELECT
    s.descricao AS servico,
    COUNT(sr.id) AS total_servicos,
    SUM(sr.valor_cobrado) AS receita,
    AVG(sr.valor_cobrado) AS ticket_medio
FROM servico_realizado sr
INNER JOIN servico s ON sr.servico_id = s.id
GROUP BY s.descricao
ORDER BY COUNT(sr.id) DESC, SUM(sr.valor_cobrado) DESC;