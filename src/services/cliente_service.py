from ..models import Cliente, Veiculo
from ..repositories import ClienteRepository
from .veiculo_service import VeiculoService
from ..utils import validar_cpf




class ClienteService:

    def __init__(self, cliente_repo: ClienteRepository, veiculo_serv: VeiculoService) -> None:
        self.cliente_repo = cliente_repo
        self.veiculo_serv = veiculo_serv


    def adicionar_cliente(self, cliente_model: Cliente, veiculo_model: Veiculo) -> int:
        try:
            # verifica se cliente existe
            if self.existe_cliente(cliente_model.cpf):
                raise ValueError(f"Já existe um cliente cadastrado com o CPF {cliente_model.cpf}.")

            # adicionar cliente
            cliente_id = self.cliente_repo.adicionar(cliente_model)

            # Verifica se veiculo existe
            veiculo_existente = self.veiculo_serv.veiculo_existe(veiculo_model.placa)
            if veiculo_existente and cliente_id:
                # muda de proprietario
                self.veiculo_serv.transferir_proprietario(cliente_id, veiculo_model.placa)
            elif cliente_id:
                # adiciona carro
                veiculo_model.cliente_id = cliente_id
                self.veiculo_serv.cadastrar_veiculo(veiculo_model)

            self.cliente_repo.db.commit() # Se tudo deu certo, salva permanentemente
            return cliente_id
        except Exception as e:
            self.cliente_repo.db.rollback() # Se algo deu errado, desfaz tudo
            raise e # Propaga o erro para a camada de CLI saber o que aconteceu
    
    def vincular_veiculo(self, cliente_model: Cliente, veiculo_model: Veiculo) -> None:

        if cliente_model.id:
            veiculo_model.cliente_id = cliente_model.id
            self.veiculo_serv.cadastrar_veiculo(veiculo_model)
            self.cliente_repo.db.commit()


    def listar_todos(self) -> list[Cliente]:
        return self.cliente_repo.listar_todos()

    def buscar_por_cpf(self, cpf: str) -> Cliente:
        if not validar_cpf(cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
        
        cliente = self.cliente_repo.buscar_cpf(cpf)

        if not cliente:
            raise ValueError(f"Não existe um cliente cadastrado com o CPF {cpf}.")
        
        return cliente 

    def listar_cpfs(self) -> list[str]:
        clientes = self.listar_todos()

        return [c.cpf for c in clientes]


    def lista_formatada(self) -> list[str]:
        clientes = self.listar_todos()

        return [f"{c.nome} ({c.cpf[:3]}.{c.cpf[3:6]}.{c.cpf[6:9]}-{c.cpf[9:11]})" for c in clientes]

    def existe_cliente(self, cpf: str) -> bool:
        try:
            self.buscar_por_cpf(cpf)
            return True
        
        except ValueError:
            return False
        
    def buscar_por_id(self, id: int) -> Cliente:
        cliente = self.cliente_repo.buscar_id(id)

        if not cliente:
            raise ValueError(f"Não existe um cliente cadastrado com o ID {id}.")
        
        return cliente
    
    def lista_busca(self) -> list[str]:
        clientes = self.listar_todos()

        return [f"{c.nome} ({c.cpf})" for c in clientes]