from ..models.servico import Servico
from ..database.database_manager import DatabaseManager
from ..utils import CAMINHO_SQL
from .base_repo import BaseRepository




class ServicoRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("servico")

    def adicionar(self, servico: Servico) -> int:
        return self.execSql(
            "adicionar.sql",
            (
                servico.descricao,
                servico.preco
            ),
        )
    
    def desativar(self, id: int) -> int:
        return self.execSql(
            "desativar.sql",
            (id,),
        )

    def listarAtivos(self) -> list:
        res: list[dict] = self.db.consultar("listar_ativos.sql")

        lista_servicos: list = [Servico(**res) for res in res]
        return lista_servicos
