-- REINICIAR TABELA
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS veiculo;
DROP TABLE IF EXISTS telefone;
DROP TABLE IF EXISTS ordem_servico;
DROP TABLE IF EXISTS servico;
DROP TABLE IF EXISTS mecanico;
DROP TABLE IF EXISTS servico_realizado;

-- CRIAR NOVAS TABELAS
CREATE TABLE cliente (
	id SERIAL PRIMARY KEY,
	nome_completo VARCHAR NOT NULL,
	cpf VARCHAR(11) UNIQUE NOT NULL,
	data_nascimento DATE NOT NULL,
	endereco VARCHAR NOT NULL
);

CREATE TABLE veiculo (
	id SERIAL PRIMARY KEY,
	placa VARCHAR UNIQUE NOT NULL,
	cor VARCHAR,
	ano INT,
	marca VARCHAR NOT NULL,
	modelo VARCHAR NOT NULL,
	cliente_id INT NOT NULL REFERENCES cliente(id)
);

CREATE TABLE telefone (
	id_cliente INT NOT NULL REFERENCES cliente(id) ON DELETE CASCADE,
	numero VARCHAR(11) NOT NULL,
	tipo VARCHAR,

	PRIMARY KEY (id_cliente, numero)
);

CREATE TABLE ordem_servico (
	id SERIAL PRIMARY KEY,
	numero_os VARCHAR UNIQUE NOT NULL,
	data_hora_abertura TIMESTAMP NOT NULL,
	data_hora_fechamento TIMESTAMP,
	quilometragem_abertura INT NOT NULL,
	veiculo_id INT NOT NULL REFERENCES veiculo(id)
);

CREATE TABLE servico (
	id SERIAL PRIMARY KEY,
	descricao VARCHAR NOT NULL,
	preco_padrao DECIMAL(10,2) NOT NULL
);

CREATE TABLE mecanico (
	id SERIAL PRIMARY KEY,
	nome_completo VARCHAR NOT NULL,
	data_contratacao DATE NOT NULL,
	salario DECIMAL(10,2) NOT NULL
);

CREATE TABLE servico_realizado (
	id SERIAL PRIMARY KEY,
	valor_cobrado DECIMAL(10,2) NOT NULL,
	data_execucao DATE NOT NULL,
	ordem_servico_id INT NOT NULL REFERENCES ordem_servico(id) DELETE ON CASCADE,
	servico_id INT NOT NULL REFERENCES servico(id),
	mecanico_id INT NOT NULL REFERENCES mecanico(id)
)

