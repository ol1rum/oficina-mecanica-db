SELECT
    m.nome_completo as mecanico,
    COUNT(m.id) as servicos_realizados,
    SUM(sr.valor_cobrado) as receita_total
FROM servico_realizado sr

INNER JOIN mecanico m ON sr.mecanico_id = m.id
GROUP BY m.nome_completo
ORDER BY COUNT(m.id) DESC, SUM(SR.valor_cobrado) DESC