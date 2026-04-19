from ..utils import CAMINHO_SQL
from ..database import DatabaseManager


class BaseRepository:

    def __init__(self, db_manager: DatabaseManager, pasta_sql: str) -> None:
        self.db = db_manager
        self.path = CAMINHO_SQL / pasta_sql

    def exec_sql(self, arquivo_sql: str, parametros: tuple = ()) -> int:
        """Executa um arquivo SQL não SELECT com os parâmetros fornecidos e retorna o id de alteração."""
        res: tuple | None = self.db.executar(base_path=self.path, arquivo_sql=arquivo_sql, parametros=parametros)
        return res[0] if res else 0
    