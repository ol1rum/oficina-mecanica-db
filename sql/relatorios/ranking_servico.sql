SELECT
    s.descricao AS servico,
    COUNT(sr.id) AS total_servicos,
    SUM(sr.valor_cobrado) AS receita,
    AVG(sr.valor_cobrado) AS ticket_medio
FROM servico_realizado sr
INNER JOIN servico s ON sr.servico_id = s.id
GROUP BY s.descricao
ORDER BY COUNT(sr.id) DESC, SUM(sr.valor_cobrado) DESC;