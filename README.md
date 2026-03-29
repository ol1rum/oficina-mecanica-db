# Modelagem de Banco de Dados: Oficina Mecânica

Projeto de banco de dados desenvolvido como requisito de avaliação para a disciplina de Banco de Dados do Centro Universitário Nobre (UNIFAN).

## 🎯 Objetivo
Resolver o problema de gerenciamento de ordens de serviço de uma oficina, garantindo a integridade dos dados e a rastreabilidade dos serviços prestados por cada mecânico.

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** PostgreSQL 18
* **Modelagem:** dbdiagram.io e Draw.io
* **Interface:** VS Code com SQLTools e pgAdmin 4

## 📌 Diferenciais do Projeto
* **Tipagem Precisa:** Uso de `DECIMAL(10,2)` para valores monetários e `TIMESTAMP` para registros temporais precisos.
* **Integridade Referencial:** Configuração rigorosa de Chaves Estrangeiras (FK) com `CASCADE` para facilitar a manutenção do ambiente de desenvolvimento.
* **Consultas Complexas:** Inclusão de scripts com `INNER JOIN` para relatórios detalhados de produtividade.

## 🚀 Como Executar
1. Crie um banco de dados chamado `oficina_db`.
2. Execute o arquivo `sql/schema.sql` para gerar as tabelas.
3. Popule o banco com dados de teste usando `sql/seed.sql`.
4. Utilize os exemplos em `sql/queries.sql` para testar a extração de dados.

---
**Desenvolvido por [Murilo](https://github.com/ol1rum)** *Estudante de Engenharia de Software – UNIFAN*