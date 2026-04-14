from ..models.servico import Servico
from .base_repo import BaseRepository
from ..database import DatabaseManager

class ServicoRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "servico")

    def adicionar(self, servico: Servico) -> int:
        return self.exec_sql("adicionar.sql", (servico.descricao, servico.preco))
    
    def mudar_disponibilidade(self, id: int, disponivel: bool) -> int:
        return self.exec_sql("atualizar_disponibilidade.sql", (disponivel, id))

    def listar_filt_disponivel(self, disponivel: bool = True) -> list:
        res: list[dict] = self.db.consultar(self.path, "listar_filt.sql", (disponivel,))

        lista_servicos: list = [Servico(**res) for res in res]
        return lista_servicos

    def alterar_preco_descricao(self, id: int, servico: Servico) -> int:
        return self.exec_sql("alterar_preco_descricao.sql", (servico.preco, servico.descricao, id))