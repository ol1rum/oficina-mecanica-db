from typing import Literal

from ..models.ordem_servico import OrdemServico
from .base_repo import BaseRepository


class OSRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("ordem_servico")

    def adicionar(self, os: OrdemServico) -> int:
        return self.execSql(
            "adicionar_cliente.sql",
            (
                os.numero_os,
                os.quilometragem_abertura,
                os.veiculo_id,
                os.cliente_id,
                os.observacoes
            ),
        )

    def listarAbertas(self):
        res = self.db.consultar("listar_abertas.sql")

        lista_os: list = [OrdemServico(**res) for res in res]
        return lista_os

    def listarFinalizadas(self):
        res = self.db.consultar("listar_finalizadas.sql")

        lista_os: list = [OrdemServico(**res) for res in res]
        return lista_os

    def mudarObs(self, observacoes: str, id: int):
        return self.execSql("mudar_obs.sql", (observacoes, id))
    
    def atualizarStatusFechamento(self, status: Literal["FINALIZADA", "CANCELADA"], id: int):
        return self.execSql("fechar_os.sql", (status, id))
