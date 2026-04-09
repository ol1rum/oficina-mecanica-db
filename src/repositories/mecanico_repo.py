from datetime import date

from ..models.mecanico import Mecanico
from ..database.database_manager import DatabaseManager
from ..utils import CAMINHO_SQL
from .base_repo import BaseRepository


class MecanicoRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("mecanico")
    
    def adicionar(self, mecanico: Mecanico) -> int:
        return self.execSql(
            "adicionar.sql",
            (
                mecanico.cpf,
                mecanico.nome,
                mecanico.data_contratacao,
                mecanico.salario
            ),
        )
    
    def listarTodos(self):
        res = self.db.consultar("listar_ativos.sql")

        lista_mecanicos: list = [Mecanico(**res) for res in res]
        return lista_mecanicos
    
    def demitir(self, id: int, data: date) -> int:
        return self.execSql(
            "demitir.sql",
            (data, id),
        )
