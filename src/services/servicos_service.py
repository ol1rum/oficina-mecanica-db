from ..models import Servico
from ..repositories import ServicoRepository


class ServicoService:
    def __init__(self, servico_repo: ServicoRepository):
        self.servico_repo = servico_repo

    def adicionar(self, servico_model: Servico) -> int:
        
        # Verifica se já existe serviço igual ativo
        s_ativos = self.listarAtivos()
        if any(s.descricao.lower() == servico_model.descricao.lower() for s in s_ativos):
            raise ValueError(f"Já existe um serviço cadastrado com a descrição {servico_model.descricao}.")

        # Verifica se já existe serviço igual desativado
        s_desativados = self.listarDesativados()
        s_existente_desativado: Servico | None = next(
            (s for s in s_desativados if s.descricao.lower() == servico_model.descricao.lower()), None
        )

        # Se existir um serviço desativado com a mesma descrição, reativa ele ao invés de criar um novo
        if s_existente_desativado and s_existente_desativado.id:
            return self.reativar(s_existente_desativado.id)
        else:
            return self.servico_repo.adicionar(servico_model)

    def listarAtivos(self) -> list[Servico]:
        return self.servico_repo.listarFiltDisponivel(True)
    
    def listarDesativados(self) -> list[Servico]:
        return self.servico_repo.listarFiltDisponivel(False)

    def reativar(self, id: int) -> int:
        return self.servico_repo.mudarDisponibilidade(id, True)

    def desativar(self, id: int) -> int:
        return self.servico_repo.mudarDisponibilidade(id, False)
    
    def alterarPrecoDescricao(self, id: int, servico_model: Servico) -> int:
        if servico_model.preco < 0:
            raise ValueError("O preço do serviço não pode ser negativo.")

        if self.servicoExiste(servico_model, self.listarAtivos()):
            raise ValueError(f"Já existe um serviço cadastrado com a descrição {servico_model.descricao}.")

        return self.servico_repo.alterarPrecoDescricao(id, servico_model)
    
    def servicoExiste(self, servico_model: Servico, lista_servico: list[Servico]) -> bool:
        return any(
            s.descricao.lower() == servico_model.descricao.lower() and s.id != servico_model.id
            for s in lista_servico
        )
    
    def listarTodos(self) -> list[Servico]:
        ativos = self.listarAtivos()
        desativados = self.listarDesativados()

        return ativos + desativados
    
