from ..utils import CAMINHO_SQL
from ..database.database_manager import DatabaseManager


class BaseRepository:

    def __init__(self, pasta_sql: str) -> None:
        self.db: DatabaseManager = DatabaseManager(CAMINHO_SQL / pasta_sql)

    def execSql(self, arquivo_sql: str, parametros: tuple = (), commit: bool = True) -> int:
        """Executa um arquivo SQL não SELECT com os parâmetros fornecidos e retorna o id de alteração."""
        res: dict = self.db.executar(arquivo_sql=arquivo_sql, parametros=parametros, autocommit=commit)
        return res[0]
    