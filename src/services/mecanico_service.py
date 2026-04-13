from datetime import date

from ..utils import validarCpf
from ..models import Mecanico
from ..repositories import MecanicoRepository


class MecanicoService:
    def __init__(self, mecanico_repo: MecanicoRepository):
        self.mecanico_repo = mecanico_repo

    def adicionar(self, mecanico_model: Mecanico) -> int:

        if not validarCpf(mecanico_model.cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
            
        return self.mecanico_repo.adicionar(mecanico_model)
    
    def listarTodos(self) -> list[Mecanico]:
        return self.mecanico_repo.listarTodos()
    
    def demitir(self, id: int, data: date | None = None) -> int:
        if not data:
            data = date.today()

        return self.mecanico_repo.demitir(id, data)
