from ..models.veiculo import Veiculo
from .base_repo import BaseRepository
from ..database import DatabaseManager


class VeiculoRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "veiculo")
        
    def adicionar(self, veiculo: Veiculo) -> int:
        return self.exec_sql(
            "adicionar.sql",
            (
                veiculo.placa,
                veiculo.cor,
                veiculo.ano,
                veiculo.marca,
                veiculo.modelo,
                veiculo.cliente_id
            )
        )
    
    def buscar_placa(self, placa: str) -> Veiculo | None:
        res: list[dict] = self.db.consultar(self.path, "buscar_placa.sql", (placa,))

        return Veiculo(**res[0]) if res else None
    
    def listar_todos(self) -> list[Veiculo]:
        res: list[dict] = self.db.consultar(self.path, "listar_todos.sql")

        lista_veiculos: list = [Veiculo(**res) for res in res]
        return lista_veiculos
    
    def transferir_proprietario(self, cliente_id: int, placa: str) -> int:
        return self.exec_sql("transferir_proprietario.sql", (cliente_id, placa))
    