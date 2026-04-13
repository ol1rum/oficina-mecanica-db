from ..models import Cliente, Veiculo
from ..repositories import ClienteRepository
from .veiculo_service import VeiculoService
from ..utils import validarCpf




class ClienteService:

    def __init__(self, cliente_repo: ClienteRepository, veiculo_serv: VeiculoService) -> None:
        self.cliente_repo = cliente_repo
        self.veiculo_serv = veiculo_serv


    def adicionarCliente(self, cliente_model: Cliente, veiculo_model: Veiculo) -> int:
        
        # verifica se cliente existe
        if self.buscarPorCpf(cliente_model.cpf):
            raise ValueError(f"Já existe um cliente cadastrado com o CPF {cliente_model.cpf}.")

        # adicionar cliente
        cliente_id = self.cliente_repo.adicionar(cliente_model)

        # Verifica se carro existe
        veiculo_existente = self.veiculo_serv.buscarPorPlaca(veiculo_model.placa)
        if veiculo_existente and cliente_id:
            # muda de proprietario
            self.veiculo_serv.transferirProprietario(cliente_id, veiculo_model.placa)

        elif cliente_id:
            # adiciona carro
            veiculo_model.cliente_id = cliente_id
            self.veiculo_serv.cadastrarVeiculo(veiculo_model)

        return cliente_id
    
    def vincularVeiculo(self, cliente_model: Cliente, veiculo_model: Veiculo) -> None:
        if cliente_model.id:
            self.veiculo_serv.transferirProprietario(cliente_model.id, veiculo_model.placa)


    def listarTodos(self) -> list[Cliente]:
        return self.cliente_repo.listarTodos()

    def buscarPorCpf(self, cpf: str) -> Cliente | None:
        if not validarCpf(cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
            
        return self.cliente_repo.buscarCpf(cpf)
