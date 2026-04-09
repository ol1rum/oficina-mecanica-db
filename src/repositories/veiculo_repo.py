from ..models.veiculo import Veiculo
from ..database.database_manager import DatabaseManager
from ..utils import CAMINHO_SQL
from .base_repo import BaseRepository


class VeiculoRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("veiculo")
        
    def adicionar(self, veiculo: Veiculo) -> int:
        return self.execSql(
            "adicionar.sql",
            (
                veiculo.placa,
                veiculo.cor,
                veiculo.ano,
                veiculo.marca,
                veiculo.modelo,
                veiculo.cliente_id
            ),
        )
    
    def buscarPlaca(self, placa: str) -> Veiculo | None:
        res: list[dict] = self.db.consultar("buscar_placa.sql", (placa,))

        return Veiculo(**res[0]) if res else None
    
    def listarTodos(self) -> list[Veiculo]:
        res: list[dict] = self.db.consultar("listar_todos.sql")

        lista_veiculos: list = [Veiculo(**res) for res in res]
        return lista_veiculos
    
    def mudarDono(self, client_id: int, veiculo_id: int) -> int:
        return self.execSql(
            "mudar_dono.sql",
            (
                client_id,
                veiculo_id
            ),
        )
    