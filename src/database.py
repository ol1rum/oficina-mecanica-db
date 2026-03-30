import psycopg
from psycopg.rows import dict_row
import os

class DatabaseManager:

    def __init__(self) -> None:
        self.caminho_sql: str = os.path.join(os.path.dirname(__file__), '..', 'sql')

        self.conn_str: str = (
            f"dbname={os.getenv('DB_NAME')} "
            f"user={os.getenv('DB_USER')} "
            f"password={os.getenv('DB_PASSWORD')} "
            f"host={os.getenv('DB_HOST')}"
        )

    def consultar(self, nome_arquivo_sql: str) -> list:
        """Ler um arquivo SQL e retornar os dados da consulta (SELECT)."""
        caminho_queries: str = os.path.join(self.caminho_sql, 'queries', nome_arquivo_sql)
        with psycopg.connect(self.conn_str, row_factory=dict_row) as conn:  #type: ignore
            with conn.cursor() as cur:
                with open(caminho_queries, 'r', encoding='utf-8') as f:
                    cur.execute(f.read())  #type: ignore
                    return cur.fetchall()


    def executar(self, nome_arquivo_sql: str, parametros: dict | None) -> None:
        """Ler um arquivo SQL e executa comandos de alteração de tabelas e dados (INSERT, UPDATE, DELETE)."""
        caminho_commands: str = os.path.join(self.caminho_sql, 'commands', nome_arquivo_sql)

        with psycopg.connect(self.conn_str) as conn:
            with conn.cursor() as cur:
                with open(caminho_commands, 'r', encoding='utf-8') as f:
                    cur.execute(f.read(), params=parametros)  #type: ignore

            conn.commit()


if __name__ == '__main__':
    print(os.path.dirname(__file__))