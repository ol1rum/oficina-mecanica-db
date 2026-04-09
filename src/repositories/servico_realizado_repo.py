from ..models.servico_realizado import ServicoRealizado
from ..database.database_manager import DatabaseManager
from ..utils import CAMINHO_SQL
from .base_repo import BaseRepository


class ServicoRealizadoRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("servico_realizado")
    
    def adicionar(self, servico_realizado: ServicoRealizado) -> int:
        sr = servico_realizado
        return self.execSql(
            "adicionar.sql",
            (
                sr.valor_cobrado,
                sr.os_id,
                sr.servico_id,
                sr.mecanico_id
            ),
        )
    
    def listarPorOs(self, os_id: int):
        res: list[dict] = self.db.consultar("listar_por_os.sql", (os_id,))

        lista_sr: list = [ServicoRealizado(**res) for res in res]
        return lista_sr
