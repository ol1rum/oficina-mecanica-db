from ..models import Servico
from ..repositories import ServicoRepository
from ..utils import formatar_moeda
from decimal import Decimal

class ServicoService:
    def __init__(self, servico_repo: ServicoRepository):
        self.servico_repo = servico_repo

    def adicionar(self, servico_model: Servico) -> None:
        """
        Adiciona um novo serviço ao banco de dados. Se já existir um serviço com a mesma descrição, ele é reativado (caso esteja desativado) ou uma exceção é lançada (caso esteja ativo).
        """
        
        # Verifica se já existe serviço igual ativo
        s_ativos = self.listar_ativos()
        if any(s.descricao.lower() == servico_model.descricao.lower() for s in s_ativos):
            raise ValueError(f"Já existe um serviço cadastrado com a descrição {servico_model.descricao}.")

        # Verifica se já existe serviço igual desativado
        s_desativados = self.listar_desativados()
        s_existente_desativado: Servico | None = next(
            (s for s in s_desativados if s.descricao.lower() == servico_model.descricao.lower()), None
        )

        # Se existir um serviço desativado com a mesma descrição, reativa ele ao invés de criar um novo
        if s_existente_desativado and s_existente_desativado.id:
            s_existente_desativado.preco = servico_model.preco
            self.__reativar(s_existente_desativado)
            self.servico_repo.db.commit()
            
        # Caso contrário, cria um novo serviço
        else:
            self.servico_repo.adicionar(servico_model)
            self.servico_repo.db.commit()

    def listar_ativos(self) -> list[Servico]:
        return self.servico_repo.listar_filt_disponivel(True)
    
    def listar_desativados(self) -> list[Servico]:
        return self.servico_repo.listar_filt_disponivel(False)

    def __reativar(self, servico: Servico) -> None:
        if servico.id:
            self.servico_repo.alterar_preco_descricao(servico.id, servico)
            self.servico_repo.mudar_disponibilidade(servico.id, True)

    def desativar(self, id: int) -> None:
        self.servico_repo.mudar_disponibilidade(id, False)
        self.servico_repo.db.commit()
    
    def alterar_preco_descricao(self, id: int, servico_model: Servico) -> int:
        if servico_model.preco < 0:
            raise ValueError("O preço do serviço não pode ser negativo.")

        if self.servico_existe(servico_model, self.listar_ativos()):
            raise ValueError(f"Já existe um serviço cadastrado com a descrição {servico_model.descricao}.")

        res = self.servico_repo.alterar_preco_descricao(id, servico_model)
        self.servico_repo.db.commit()
        return res
    
    def servico_existe(self, servico_model: Servico, lista_servico: list[Servico]) -> bool:
        return any(
            s.descricao.lower() == servico_model.descricao.lower() and s.id != servico_model.id
            for s in lista_servico
        )
    
    def listar_todos(self) -> list[Servico]:
        ativos = self.listar_ativos()
        desativados = self.listar_desativados()

        return ativos + desativados
    
    def lista_formatada(self, lista_servico: list[Servico]):
        return [f"{s.descricao} - R${formatar_moeda(s.preco)}" for s in lista_servico]

    def listar_descricao(self, lista_servicos: list[Servico]) -> list[str]:
        return [s.descricao for s in lista_servicos]

    def buscar_por_id(self, id: int) -> Servico:
        servico = self.servico_repo.buscar_id(id)
        if not servico:
            raise ValueError(f"Não existe um serviço cadastrado com o ID {id}.")
        return servico