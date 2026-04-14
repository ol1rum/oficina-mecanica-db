from .base_repo import BaseRepository
from ..database import DatabaseManager


class RelatorioRepositoy(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "relatorios")

    def custo_mecanicos(self):
        return self.db.consultar(self.path, "custo_mecanico.sql")
    

    def eficiencia_mecanicos(self):
        return self.db.consultar(self.path, "eficiencia_mecanico.sql")
    
    def ranking_servicos(self):
        return self.db.consultar(self.path, "ranking_servico.sql")
    
    def receita_total(self):
        return self.db.consultar(self.path, "receita_total.sql")[0]
    
    def servicos_realizados(self):
        return self.db.consultar(self.path, "servicos_realizados.sql")
    