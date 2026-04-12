from ..models.servico import Servico
from ..database.database_manager import DatabaseManager
from ..utils import CAMINHO_SQL
from .base_repo import BaseRepository




class ServicoRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("servico")

    def adicionar(self, servico: Servico) -> int:
        return self.execSql(
            "adicionar.sql",
            (
                servico.descricao,
                servico.preco
            ),
        )
    
    def mudarDisponibilidade(self, id: int, disponivel: bool) -> int:
        return self.execSql(
            "desativar.sql",
            (disponivel, id),
        )

    def listarFiltDisponivel(self, disponivel: bool = True) -> list:
        res: list[dict] = self.db.consultar("listar_filt.sql", (disponivel,))

        lista_servicos: list = [Servico(**res) for res in res]
        return lista_servicos

    def reativar(self, id: int) -> int:
        return self.execSql(
            "reativar.sql",
            (id,),
        )
    
    def alterarPrecoDescricao(self, id: int, servico: Servico) -> int:
        return self.execSql(
            "alterar_preco_descricao.sql",
            (
                servico.preco,
                servico.descricao,
                id
            ),
        )