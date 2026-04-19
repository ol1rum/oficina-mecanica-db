SELECT 
    SUM(sr.valor_cobrado) AS receita_total,
    AVG(sr.valor_cobrado) AS ticket_medio
FROM servico_realizado sr;