from typing import Literal, Any

from ..models.ordem_servico import OrdemServico, OSDetalhada
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

    def listar_por_status(self, status: Literal["EM EXECUÇÃO", "FINALIZADA", "CANCELADA"]) -> list[OrdemServico]:
        res = self.db.consultar(self.path, "listar_por_status.sql", (status,))
        return [OrdemServico(**r) for r in res]


    def mudar_obs(self, observacoes: str, id: int) -> int:
        return self.exec_sql("mudar_obs.sql", (observacoes, id))
    
    def atualizar_status_fechamento(self, status: Literal["FINALIZADA", "CANCELADA"], id: int) -> int:
        return self.exec_sql("fechar_os.sql", (status, id))

    def buscar_por_id(self, id: int) -> OrdemServico | None:
        res = self.db.consultar(self.path, "buscar_por_id.sql", (id,))

        return OrdemServico(**res[0]) if res else None
    
    def detalhes_os(self, id: int) -> OSDetalhada | None:
        res = self.db.consultar(self.path, "detalhes_os.sql", (id,))

        return OSDetalhada(**res[0]) if res else None