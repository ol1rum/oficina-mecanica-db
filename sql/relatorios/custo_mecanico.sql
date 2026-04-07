-- CUSTO TOTAL COM MECANICOS
SELECT
    COUNT(m.id) AS total_mecanico,
    SUM(m.salario) AS custo_total,
    AVG(m.salario) AS media_salario
FROM mecanico m;