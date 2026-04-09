from .base_repo import BaseRepository


class RelatorioRepositoy(BaseRepository):

    def __init__(self) -> None:
        super().__init__("relatorios")

    def custoMecanicos(self):
        return self.db.consultar("custo_mecanicos.sql")
    

    def eficienciaMecanicos(self):
        return self.db.consultar("eficiencia_mecanico.sql")
    
    def rankingServicos(self):
        return self.db.consultar("ranking_servico.sql")
    
    def receitaTotal(self):
        return self.db.consultar("receita_total.sql")[0]
    
    def servicosRealizados(self):
        return self.db.consultar("servicos_realizados.sql")
    