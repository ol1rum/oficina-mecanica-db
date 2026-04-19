from ..models import Veiculo
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
        resultado: list[dict] = self.db.consultar(self.path, "buscar_placa.sql", (placa,))

        return Veiculo(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Veiculo]:
        resultado: list[dict] = self.db.consultar(self.path, "listar_todos.sql")

        lista_veiculos: list = [Veiculo(**v) for v in resultado]
        return lista_veiculos
    
    def transferir_proprietario(self, cliente_id: int, placa: str) -> int:
        return self.exec_sql("transferir_proprietario.sql", (cliente_id, placa))
    
    def buscar_por_cliente(self, clietne_id) -> list[Veiculo]:
        resultado: list[dict] = self.db.consultar(self.path, "buscar_por_cliente.sql", (clietne_id,))

        return [Veiculo(**v) for v in resultado]

    def buscar_id(self, id: int) -> Veiculo | None:
        resultado: list[dict] = self.db.consultar(self.path, "buscar_id.sql", (id,))
        return Veiculo(**resultado[0]) if resultado else None