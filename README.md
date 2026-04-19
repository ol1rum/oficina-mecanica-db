# Sistema de Gestão: Oficina Mecânica

Projeto de banco de dados e aplicação CLI desenvolvido como requisito de avaliação para a disciplina de Banco de Dados do Centro Universitário Nobre (UNIFAN).

## 🎯 Objetivo
Resolver o problema de gerenciamento de ordens de serviço de uma oficina, garantindo a integridade dos dados, rastreabilidade dos serviços prestados por mecânicos e provendo uma interface amigável para o usuário final.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Banco de Dados:** PostgreSQL (Dockerizado)
* **Bibliotecas Principais:** 
  * `psycopg`: Para conexão e transações com o banco.
  * `questionary`: Para a interface interativa de linha de comando (CLI).
  * `python-dotenv`: Para gerenciamento de credenciais (arquivo `.env`).
* **Padrões de Projeto:** Arquitetura em camadas utilizando *Repository Pattern* e *Service Layer*.

## 🐳 Rodando com Docker (Recomendado)
A forma mais fácil de rodar o projeto é utilizando o Docker, que já configura o banco de dados e as tabelas automaticamente.

1.  **Inicie o banco de dados:**
    ```bash
    docker compose up -d
    ```
2.  **Configure o arquivo `.env`:**
    Certifique-se de que as credenciais no seu `.env` coincidem com as do `docker-compose.yml` (veja a seção de configuração abaixo).
3.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

## 🚀 Como Executar Manualmente

### Pré-requisitos
* Python 3 instalado.
* PostgreSQL rodando localmente.
* Gerenciador de pacotes `uv` (recomendado) ou `pip`.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ol1rum/oficina-mecanica-db.git
   cd oficina-mecanica-db
   ```

2. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   DB_HOST=localhost
   DB_NAME=oficina_db
   DB_USER=user_oficina
   DB_PASSWORD=password_oficina
   DB_PORT=5432
   ```

3. **Instale as dependências:**
   ```bash
   uv sync
   ```

4. **Inicie a Aplicação:**
   ```bash
   python main.py
   ```

## 📂 Modelagem de Dados (Diagramas)
* [Modelo Conceitual](./diagramas/modelo_conceitual.png)
* [Modelo Lógico](./diagramas/modelo_logico.png)

---
**Desenvolvido por [Murilo](https://github.com/ol1rum)** *Estudante de Engenharia de Software – UNIFAN*