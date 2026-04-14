from psycopg.rows import dict_row
import psycopg
import os
from dotenv import load_dotenv
from pathlib import Path
from threading import Lock

class DatabaseManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            load_dotenv()
            try:
                self.conn = psycopg.connect(
                    host=os.getenv("DB_HOST"), dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                    port=os.getenv("DB_PORT", 5432)
                )
                self._initialized = True
            except Exception as e:
                print(f"FATAL: Erro ao conectar ao banco de dados: {e}")
                raise

    def _get_sql(self, base_path: Path, arquivo_sql: str) -> str:
        caminho_completo = base_path / arquivo_sql
        with open(caminho_completo, 'r', encoding='utf-8') as f:
            return f.read()

    def consultar(self, base_path: Path, arquivo_sql: str, parametros: tuple = ()):
        query = self._get_sql(base_path, arquivo_sql)
        with self.conn.cursor(row_factory=dict_row) as cur:
            cur.execute(query, parametros)  #type: ignore
            return cur.fetchall()

    def executar(self, base_path: Path, arquivo_sql: str, parametros: tuple = ()):
        query = self._get_sql(base_path, arquivo_sql)
        with self.conn.cursor() as cur:
            cur.execute(query, parametros)  #type: ignore
            return cur.fetchone() if cur.description else None

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()
