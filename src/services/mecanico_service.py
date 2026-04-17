from datetime import date

from ..utils import validar_cpf
from ..models import Mecanico
from ..repositories import MecanicoRepository


class MecanicoService:
    def __init__(self, mecanico_repo: MecanicoRepository):
        self.mecanico_repo = mecanico_repo

    def adicionar(self, mecanico_model: Mecanico) -> None:
        """
        Adiciona um novo mecânico ao sistema. Se um mecânico com o mesmo CPF já existir e estiver ativo, lança um erro.
        """

        # valida o cpf
        if not validar_cpf(mecanico_model.cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
        
        # verifica se já existe um mecanico com o mesmo cpf
        mecanico_existe = self.mecanico_inativo(mecanico_model.cpf)

        # caso exista e não tenha sido demitido sobe um erro
        if mecanico_existe:
            mecanico_existeste = self.buscar_por_cpf(mecanico_model.cpf)

            if not mecanico_existeste.data_demissao:
                raise ValueError(f"Já existe um mecanico ativo cadastrado com o CPF {mecanico_model.cpf}.")

            # atualiza possiveis alterações
            mecanico_existeste.nome = mecanico_model.nome
            mecanico_existeste.data_contratacao = mecanico_model.data_contratacao
            mecanico_existeste.salario = mecanico_model.salario
        
            if mecanico_existeste and mecanico_existeste.id and mecanico_existeste.data_contratacao:
                self.mecanico_repo.recontratar(mecanico_existeste)
        
        else:
            self.mecanico_repo.adicionar(mecanico_model)

        self.mecanico_repo.db.commit()
    
    def listar_todos(self) -> list[Mecanico]:
        return self.mecanico_repo.listar_todos()
    
    def demitir(self, id: int, data: date | None = None) -> int:
        if not data:
            data = date.today()

        mecanico_id = self.mecanico_repo.demitir(id, data)
        self.mecanico_repo.db.commit()

        return mecanico_id
    
    def mecanico_inativo(self, cpf: str) -> bool:
        try:
            mec = self.buscar_por_cpf(cpf)
            return True if mec.data_demissao else False
        
        except ValueError:
            return False
    
    def mecanico_ativo(self, cpf: str) -> bool:
        try:
            mec = self.buscar_por_cpf(cpf)
            return True if not mec.data_demissao else False
        
        except ValueError:
            return False

    def buscar_por_cpf(self, cpf: str) -> Mecanico:
        mecanico = self.mecanico_repo.buscar_cpf(cpf)

        if not mecanico:
            raise ValueError(f"Não existe um mecanico cadastrado com o CPF {cpf}.")
        
        return mecanico
    
    def buscar_por_id(self, id: int) -> Mecanico:
        mecanico = self.mecanico_repo.buscar_id(id)

        if not mecanico:
            raise ValueError(f"Não existe um mecanico cadastrado com o ID {id}.")
        
        return mecanico
    
    def listar_cpfs(self) -> list[str]:
        mecanicos = self.listar_todos()

        return [m.cpf for m in mecanicos]
    
    def lista_busca(self):
        mecanicos = self.listar_todos()

        return [f"{m.nome} ({m.cpf})" for m in mecanicos]
    
    def listar_ativos(self) -> list[Mecanico]:
        lista_mecanicos = self.listar_todos()
        return [m for m in lista_mecanicos if m.data_demissao is None]
    
    def listar_demitidos(self) -> list[Mecanico]:
        lista_mecanicos = self.listar_todos()
        return [m for m in lista_mecanicos if m.data_demissao is not None]
    
    def lista_formatada(self):
        lista_mecanicos = self.listar_todos()
        return [f"{m.nome} ({m.cpf})" for m in lista_mecanicos]