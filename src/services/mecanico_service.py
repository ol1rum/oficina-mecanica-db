from datetime import date

from ..utils import validar_cpf
from ..models import Mecanico
from ..repositories import MecanicoRepository


class MecanicoService:
    def __init__(self, mecanico_repo: MecanicoRepository):
        self.mecanico_repo = mecanico_repo

    def adicionar(self, mecanico_model: Mecanico) -> int:

        if not validar_cpf(mecanico_model.cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
            
        mecanico_id = self.mecanico_repo.adicionar(mecanico_model)
        self.mecanico_repo.db.commit()

        return mecanico_id
    
    def listar_todos(self) -> list[Mecanico]:
        return self.mecanico_repo.listar_todos()
    
    def demitir(self, id: int, data: date | None = None) -> int:
        if not data:
            data = date.today()

        mecanico_id = self.mecanico_repo.demitir(id, data)
        self.mecanico_repo.db.commit()

        return mecanico_id
