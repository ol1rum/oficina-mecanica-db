from typing import Literal

from ..models.ordem_servico import OrdemServico
from .base_repo import BaseRepository
from ..database import DatabaseManager

class OSRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "ordem_servico")

    def adicionar(self, os: OrdemServico) -> int:
        return self.exec_sql(
            "adicionar_os.sql",
            (
                os.numero_os,
                os.quilometragem_abertura,
                os.veiculo_id,
                os.cliente_id,
                os.observacoes,
            )
        )

    def listar_abertas(self):
        res = self.db.consultar(self.path, "listar_abertas.sql")

        lista_os: list = [OrdemServico(**res) for res in res]
        return lista_os

    def listar_finalizadas(self):
        res = self.db.consultar(self.path, "listar_finalizadas.sql")

        lista_os: list = [OrdemServico(**res) for res in res]
        return lista_os

    def mudar_obs(self, observacoes: str, id: int):
        return self.exec_sql("mudar_obs.sql", (observacoes, id))
    
    def atualizar_status_fechamento(self, status: Literal["FINALIZADA", "CANCELADA"], id: int):
        return self.exec_sql("fechar_os.sql", (status, id))
