from ..models import OrdemServico, ServicoRealizado
from ..repositories import OSRepository, ServicoRealizadoRepository


class OrdemServicoService:

    def __init__(self, os_repo: OSRepository, sr_repo: ServicoRealizadoRepository) -> None:
        self.os_repo = os_repo
        self.sr_repo = sr_repo

    def abrir_os(self, os_model: OrdemServico) -> int:
        os_id = self.os_repo.adicionar(os_model)
        self.os_repo.db.commit()
        return os_id
    
    def add_servico_realizado(self, sr_model: ServicoRealizado) -> int:
        oss_abertas = self.os_repo.listar_abertas()
        if not any(os.id == sr_model.os_id for os in oss_abertas):
            raise ValueError(f"A OS {sr_model.os_id} não está aberta.")

        sr_id = self.sr_repo.adicionar(sr_model)
        self.sr_repo.db.commit()
        return sr_id
    
    def alterar_observacoes(self, id: int, observacoes: str) -> int:
        res = self.os_repo.mudar_obs(observacoes, id)
        self.os_repo.db.commit()
        return res
    
    def finalizar_os(self, id: int) -> int:
        res = self.os_repo.atualizar_status_fechamento('FINALIZADA', id)
        self.os_repo.db.commit()
        return res
    
    def cancelar_os(self, id: int) -> int:
        res = self.os_repo.atualizar_status_fechamento('CANCELADA', id)
        self.os_repo.db.commit()
        return res
    

    