from pathlib import Path

import psycopg
from psycopg.rows import dict_row, DictRow
from psycopg.rows import dict_row
from typing import cast, LiteralString
import os


class DatabaseManager:

    def __init__(self, pasta_base: Path) -> None:
        self.conn_str: str = (
            f"dbname={os.getenv('DB_NAME')} "
            f"user={os.getenv('DB_USER')} "
            f"password={os.getenv('DB_PASSWORD')} "
            f"host={os.getenv('DB_HOST')}"
        )
        self.pasta_base: Path = pasta_base

    def consultar(self, arquivo_sql: str, parametros: tuple | None = None) -> list:
        """Ler um arquivo SQL e retornar os dados da consulta (SELECT)."""

        with psycopg.connect(self.conn_str, row_factory=dict_row) as conn: # type: ignore
            with conn.cursor() as cur:
                with open(self.pasta_base / arquivo_sql, 'r', encoding='utf-8') as f:
                    query = cast(LiteralString, f.read())
                    cur.execute(query, params=parametros)
                    return cur.fetchall()


    def executar(self, arquivo_sql: str, parametros: tuple | None = None, autocommit: bool = True) -> dict:
        """Ler um arquivo SQL e executa comandos de alteração de tabelas e dados (INSERT, UPDATE, DELETE)."""

        with psycopg.connect(self.conn_str) as conn:
            with conn.cursor() as cur:
                with open(self.pasta_base / arquivo_sql, 'r', encoding='utf-8') as f:
                    query = cast(LiteralString, f.read())
                    cur.execute(query, params=parametros)
                    
                    if autocommit:
                        conn.commit()
                    else:
                        conn.rollback()

                    return cur.fetchone() if cur.description else {}  #type: ignore


if __name__ == '__main__':
    print(os.path.dirname(__file__))