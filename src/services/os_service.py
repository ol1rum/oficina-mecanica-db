from ..models import OrdemServico, ServicoRealizado
from ..repositories import OSRepository, ServicoRealizadoRepository


class OrdemServicoService:

    def __init__(self, os_repo: OSRepository, sr_repo: ServicoRealizadoRepository) -> None:
        self.os_repo = os_repo
        self.sr_repo = sr_repo

    def abrirOS(self, os_model: OrdemServico) -> int:
        return self.os_repo.adicionar(os_model)
    
    def addServicoRealizado(self, sr_model: ServicoRealizado) -> int:
        oss_abertas = self.os_repo.listarAbertas()
        if not any(os.id == sr_model.os_id for os in oss_abertas):
            raise ValueError(f"A OS {sr_model.os_id} não está aberta.")

        return self.sr_repo.adicionar(sr_model)
    
    def alterarObservacoes(self, id: int, observacoes: str) -> int:
        return self.os_repo.mudarObs(observacoes, id)
    
    def finalizarOS(self, id: int) -> int:
        return self.os_repo.atualizarStatusFechamento('FINALIZADA', id)
    
    def cancelarOS(self, id: int) -> int:
        return self.os_repo.atualizarStatusFechamento('CANCELADA', id)
    

    