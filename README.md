# Sistema de Gestão: Oficina Mecânica

Projeto de banco de dados e aplicação CLI desenvolvido como requisito de avaliação para a disciplina de Banco de Dados do Centro Universitário Nobre (UNIFAN).

## 🎯 Objetivo
Resolver o problema de gerenciamento de ordens de serviço de uma oficina, garantindo a integridade dos dados, rastreabilidade dos serviços prestados por mecânicos e provendo uma interface amigável para o usuário final.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Banco de Dados:** PostgreSQL
* **Bibliotecas Principais:** 
  * `psycopg`: Para conexão e transações com o banco.
  * `questionary`: Para a interface interativa de linha de comando (CLI).
  * `python-dotenv`: Para gerenciamento de credenciais (arquivo `.env`).
* **Padrões de Projeto:** Arquitetura em camadas utilizando *Repository Pattern* e *Service Layer*.
* **Modelagem:** dbdiagram.io e Draw.io

## 📌 Diferenciais do Projeto
* **Interface CLI Interativa:** Menus navegáveis, validações em tempo real (ex: CPF e formato de data) e paginação de listas.
* **Arquitetura Limpa:** Separação clara entre acesso a dados (`repositories`), regras de negócio (`services`) e interação com o usuário (`cli`).
* **Gestão Completa de OS:** Fluxo completo desde a abertura, adição de serviços realizados por mecânicos específicos, até a finalização e cancelamento.
* **Integridade de Dados:** Validações para impedir CPFs duplicados e tratamento seguro de transações SQL (commit/rollback).

## 📂 Modelagem de Dados (Diagramas)
Os modelos conceituais e lógicos do banco de dados podem ser visualizados abaixo:

* [Modelo Conceitual](./diagramas/modelo_conceitual.png)
* [Modelo Lógico](./diagramas/modelo_logico.png)

## 🚀 Como Executar

### Pré-requisitos
* Python 3 instalado.
* PostgreSQL rodando localmente ou em servidor.
* Gerenciador de pacotes `uv` (recomendado) ou `pip`.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ol1rum/oficina-mecanica-db.git
   cd oficina-mecanica-db
   ```

2. **Configure o Banco de Dados:**
   * Crie um banco de dados no PostgreSQL (ex: `oficina_db`).
   * Execute o script `sql/schema.sql` para criar as tabelas.
   * (Opcional) Execute `sql/seed.sql` para popular com dados iniciais.

3. **Configure as Variáveis de Ambiente:**
   * Crie um arquivo `.env` na raiz do projeto com base no modelo abaixo:
     ```env
     DB_HOST=localhost
     DB_NAME=oficina_db
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_PORT=5432
     ```

4. **Instale as dependências:**
   ```bash
   uv sync
   # ou via pip: pip install -r requirements.txt (se aplicável)
   ```

5. **Inicie a Aplicação:**
   ```bash
   python main.py
   ```

---
**Desenvolvido por [Murilo](https://github.com/ol1rum)** *Estudante de Engenharia de Software – UNIFAN*