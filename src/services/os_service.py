from ..models import OrdemServico, ServicoRealizado, OSDetalhada
from ..repositories import OSRepository, ServicoRealizadoRepository
from typing import Any

from datetime import datetime


class OrdemServicoService:

    def __init__(self, os_repo: OSRepository, sr_repo: ServicoRealizadoRepository) -> None:
        self.os_repo = os_repo
        self.sr_repo = sr_repo

    def abrir_os(self, os_model: OrdemServico) -> int:
        os_model.numero_os = datetime.now().strftime("%d%m%Y%H%M%S%f")[:-3]

        os_id = self.os_repo.adicionar(os_model)
        self.os_repo.db.commit()
        return os_id
    
    def add_servico_realizado(self, sr_model: ServicoRealizado) -> int:
        oss_abertas = self.listar_abertas()
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
    
    def opcoes_os_finalizadas(self) -> dict[int, str]:
        lista = self.listar_finalizadas() + self.listar_canceladas()

        dict_formatado = {
            os.id:f"{os.numero_os} - {os.data_hora_abertura.strftime('%d/%m/%Y %H:%M')}"
            for os in lista if os.id is not None and os.data_hora_abertura is not None
        }
        
        return dict_formatado

    def buscar_por_id(self, id: int) -> OrdemServico:
        os = self.os_repo.buscar_por_id(id)
        if not os:
            raise ValueError(f"Não existe uma Ordem de Serviço cadastrada com o ID {id}.")
        
        return os

    def buscar_sr_por_id(self, id: int) -> ServicoRealizado:
        sr = self.sr_repo.buscar_id(id)
        if not sr:
            raise ValueError(f"Não existe um serviço realizado cadastrado com o ID {id}.")
        return sr

        
    def listar_abertas(self) -> list[OrdemServico]:
        return self.os_repo.listar_por_status("EM EXECUÇÃO")
    
    def listar_finalizadas(self) -> list[OrdemServico]:
        return self.os_repo.listar_por_status("FINALIZADA")

    def listar_canceladas(self) -> list[OrdemServico]:
        return self.os_repo.listar_por_status("CANCELADA")
    
    def detalhes_os(self, id: int) -> OSDetalhada:
        det_os = self.os_repo.detalhes_os(id)

        if not det_os:
            raise ValueError(f"Não existe uma Ordem de Serviço cadastrada com o ID {id}.")
        
        return det_os  #type: ignore
    def opcoes_os_abertas(self) -> dict[int, str]:
        lista = self.listar_abertas()

        dict_formatado = {
            os.id:f"{os.numero_os} - {os.data_hora_abertura.strftime('%d/%m/%Y %H:%M')}"
            for os in lista if os.id is not None and os.data_hora_abertura is not None
        }
        
        return dict_formatado