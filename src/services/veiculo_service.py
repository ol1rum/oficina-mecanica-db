from ..models import Veiculo, Cliente
from ..repositories import VeiculoRepository


class VeiculoService:
    def __init__(self, veiculo_repo: VeiculoRepository):
        self.veiculo_repo = veiculo_repo

    def cadastrarVeiculo(self, veiculo_model: Veiculo) -> int:
        if self.veiculo_repo.buscarPlaca(veiculo_model.placa):
            raise ValueError(f"Já existe um veículo cadastrado com a placa {veiculo_model.placa}.")
        
        if not veiculo_model.cliente_id:
            raise ValueError("O ID do cliente não pode ser nulo.")

        return self.veiculo_repo.adicionar(veiculo_model)
    
    def buscarPorPlaca(self, placa: str) -> Veiculo | None:
        return self.veiculo_repo.buscarPlaca(placa)
    
    def listarVeiculos(self) -> list[Veiculo]:
        return self.veiculo_repo.listarTodos()
    
    def transferirProprietario(self, cliente_id: int, placa: str) -> None:
        self.veiculo_repo.transferirProprietario(cliente_id, placa)