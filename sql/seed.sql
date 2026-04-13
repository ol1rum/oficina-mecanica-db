-- POVOANDO CLIENTES
INSERT INTO cliente (cpf, data_nascimento, nome_completo, endereco) VALUES
    ('12345678901', '1995-05-20', 'Murilo Oliveira', 'Rua B, Feira de Santana - BA'),
    ('98765432100', '1992-08-15', 'Larissa Oliveira', 'Av. Getúlio Vargas, Feira de Santana - BA');

-- POVOANDO TELEFONES
INSERT INTO telefone (cliente_id, numero, tipo) VALUES
    (1, '75999991234', 'Celular'),
    (1, '7533221100', 'Fixo'),
    (2, '75988884321', 'Trabalho');

-- POVOANDO VEÍCULOS
INSERT INTO veiculo (placa, cor, ano, marca, modelo, cliente_id) VALUES
    ('FSA-1234', 'Prata', 2022, 'Honda', 'Civic', 1),
    ('BAH-5050', 'Branco', 2019, 'Fiat', 'Argo', 2),
    ('REI-1990', 'Vermelho', 2023, 'Toyota', 'Corolla', 1);

-- POVOANDO MECÂNICOS
INSERT INTO mecanico (cpf, nome_completo, data_contratacao, salario) VALUES
    ('11122233344', 'Seu Jorge Mecânico', '2020-01-10', 3500.00),
    ('55566677788', 'Tiago Alinhador', '2023-06-15', 2800.00);

-- POVOANDO SERVIÇOS
INSERT INTO servico (descricao, preco_padrao) VALUES
    ('Troca de Óleo e Filtro', 250.00),
    ('Alinhamento e Balanceamento', 120.00),
    ('Limpeza de Bicos', 180.00),
    ('Revisão Geral', 500.00);

-- POVOANDO ORDENS DE SERVIÇO
INSERT INTO ordem_servico (
    numero_os,
    data_hora_abertura,
    data_hora_fechamento,
    quilometragem_abertura,
    veiculo_id,
    cliente_id,
    observacoes,
    status
) VALUES ('OS-2026-001', '2026-04-01 09:00:00', '2026-04-01 16:30:00', 45000, 2, 2, 'Revisão de rotina para viagem.', 'FINALIZADA');

-- Uma OS aberta (Em execução)
INSERT INTO ordem_servico (
    numero_os,
    data_hora_abertura,
    quilometragem_abertura,
    veiculo_id,
    cliente_id,
    observacoes,
    status
) VALUES ('OS-2026-002', CURRENT_TIMESTAMP, 12500, 1, 1, 'Barulho na suspensão dianteira ao passar em buracos.', 'EM EXECUÇÃO');

-- POVOANDO SERVIÇOS REALIZADOS
-- Serviços da OS Fechada
INSERT INTO servico_realizado (valor_cobrado, data_execucao, ordem_servico_id, servico_id, mecanico_id) VALUES
    (250.00, '2026-04-01', 1, 1, 1),
    (120.00, '2026-04-01', 1, 2, 2);

-- Serviços da OS Aberta (Vinculando um serviço já feito nela)
INSERT INTO servico_realizado (valor_cobrado, data_execucao, ordem_servico_id, servico_id, mecanico_id) VALUES
    (180.00, CURRENT_DATE, 2, 3, 1);