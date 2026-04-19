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
    
    def listar_todos(self) -> list[Mecanico]:
        res = self.db.consultar(self.path, "listar_todos.sql")

        lista_mecanicos: list = [Mecanico(**res) for res in res]
        return lista_mecanicos
    
    def demitir(self, id: int, data: date) -> int:
        return self.exec_sql(
            "demitir.sql",
            (data, id),
        )

    def buscar_cpf(self, cpf: str) -> Mecanico | None:
        res: list[dict] = self.db.consultar(self.path, "buscar_cpf.sql", (cpf,))

        return Mecanico(**res[0]) if res else None
    
    def buscar_id(self, id: int) -> Mecanico | None:
        res: list[dict] = self.db.consultar(self.path, "buscar_id.sql", (id,))

        return Mecanico(**res[0]) if res else None
    
    def recontratar(self, mecanico_model: Mecanico) -> int:

        if mecanico_model.id:
            return self.exec_sql(
                "recontratar.sql",
                (
                    mecanico_model.nome,
                    mecanico_model.data_contratacao,
                    mecanico_model.salario,
                    mecanico_model.cpf,
                )
            )
        
        else:
            raise ValueError("Mecanico não encontrado.")