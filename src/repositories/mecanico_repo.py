from datetime import date

from ..models.mecanico import Mecanico
from .base_repo import BaseRepository
from ..database import DatabaseManager

class MecanicoRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "mecanico")
    
    def adicionar(self, mecanico: Mecanico) -> int:
        return self.exec_sql(
            "adicionar.sql",
            (
                mecanico.cpf,
                mecanico.nome,
                mecanico.data_contratacao,
                mecanico.salario
            )
        )
    
    def listar_todos(self):
        res = self.db.consultar(self.path, "listar_ativos.sql")

        lista_mecanicos: list = [Mecanico(**res) for res in res]
        return lista_mecanicos
    
    def demitir(self, id: int, data: date) -> int:
        return self.exec_sql(
            "demitir.sql",
            (data, id),
        )
