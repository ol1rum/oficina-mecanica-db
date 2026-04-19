from ..models.servico_realizado import ServicoRealizado
from .base_repo import BaseRepository
from ..database import DatabaseManager

class ServicoRealizadoRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "servico_realizado")
    
    def adicionar(self, servico_realizado: ServicoRealizado) -> int:
        sr = servico_realizado
        return self.exec_sql(
            "adicionar.sql",
            (
                sr.valor_cobrado,
                sr.os_id,
                sr.servico_id,
                sr.mecanico_id
            )
        )
    
    def listar_por_os(self, os_id: int):
        res: list[dict] = self.db.consultar(self.path, "listar_por_os.sql", (os_id,))

        lista_sr: list = [ServicoRealizado(**res) for res in res]
        return lista_sr

    def buscar_id(self, id: int) -> ServicoRealizado | None:
        res: list[dict] = self.db.consultar(self.path, "buscar_id.sql", (id,))
        return ServicoRealizado(**res[0]) if res else None
