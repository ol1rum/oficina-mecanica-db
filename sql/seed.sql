INSERT INTO cliente (nome_completo, cpf, data_nascimento, endereco) VALUES
    ('João da Silva', '12345678901', '1990-05-15', 'Rua A, 1'),
    ('Maria Santos', '98765432109', '1985-08-22', 'Avenida B, 20'),
    ('Carlos Oliveira', '45678901234', '1992-03-10', 'Rua C, 5'),
    ('Ana Souza', '32109876543', '1988-11-25', 'Avenida D, 15'),
    ('Pedro Almeida', '78901234567', '1995-07-08', 'Rua E, 8');

INSERT INTO veiculo (placa, cor, ano, marca, modelo, cliente_id) VALUES
    ('ABC1234', 'Azul', 2018, 'Toyota', 'Corolla', 1),
    ('XYZ5678', 'Preto', 2020, 'Honda', 'Civic', 2),
    ('DEF9876', 'Branco', 2019, 'Ford', 'Focus', 3),
    ('GHI5432', 'Vermelho', 2017, 'Chevrolet', 'Onix', 4),
    ('JKL1357', 'Prata', 2016, 'Volkswagen', 'Gol', 5),
    ('OIH8426', 'Preto', 2021, 'Fiat', 'Uno', 1),
    ('QWE2468', 'Cinza', 2015, 'Renault', 'Sandero', 2);

INSERT INTO telefone (id_cliente, numero, tipo) VALUES
    (1, '12345678901', 'Celular'),
    (2, '98765432109', 'Residencial'),
    (3, '45678901234', 'Celular'),
    (4, '32109876543', 'Comercial'),
    (5, '78901234567', 'Celular'),
    (3, '55555555555', 'Residencial'),
    (2, '44444444444', 'Comercial');

INSERT INTO ordem_servico (numero_os, data_hora_abertura, data_hora_fechamento, quilometragem_abertura, veiculo_id) VALUES
    ('OS001', '2023-09-01 10:00:00', '2023-09-01 12:30:00', 10000, 1),
    ('OS002', '2023-09-02 14:30:00', '2023-09-02 16:45:00', 15000, 2),
    ('OS003', '2023-09-03 09:15:00', '2023-09-03 11:00:00', 20000, 3),
    ('OS004', '2023-09-04 13:00:00', '2023-09-04 15:30:00', 25000, 4),
    ('OS005', '2023-09-05 08:45:00', '2023-09-05 10:30:00', 30000, 5),
    ('OS006', '2023-09-06 11:30:00', '2023-09-06 13:45:00', 12000, 6),
    ('OS007', '2023-09-07 15:00:00', '2023-09-07 17:15:00', 18000, 7);

INSERT INTO servico (descricao, preco_padrao) VALUES
    ('Troca de óleo', 50.00),
    ('Alinhamento e balanceamento', 100.00),
    ('Revisão completa', 200.00),
    ('Troca de pastilhas de freio', 80.00),
    ('Troca de filtro de ar', 30.00);

INSERT INTO mecanico (nome_completo, data_contratacao, salario) VALUES
    ('José Ferreira', '2015-06-01', 3000.00),
    ('Maria Lima', '2017-09-15', 3200.00),
    ('Carlos Pereira', '2018-11-20', 2800.00),
    ('Ana Costa', '2020-01-10', 3500.00),
    ('Pedro Santos', '2019-04-25', 3100.00);

INSERT INTO servico_realizado (valor_cobrado, data_execucao, ordem_servico_id, servico_id, mecanico_id) VALUES
    (50.00, '2023-09-02', 1, 1, 1),
    (100.00, '2023-09-03', 2, 2, 2),
    (200.00, '2023-09-03', 3, 3, 3),
    (80.00, '2023-09-05', 4, 4, 4),
    (30.00, '2023-09-07', 5, 5, 5),
    (100.00, '2023-09-07', 6, 2, 1),
    (150.00, '2023-09-07', 7, 3, 2);
