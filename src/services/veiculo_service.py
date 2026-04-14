from ..models import Veiculo, Cliente
from ..repositories import VeiculoRepository


class VeiculoService:
    def __init__(self, veiculo_repo: VeiculoRepository):
        self.veiculo_repo = veiculo_repo

    def cadastrar_veiculo(self, veiculo_model: Veiculo) -> int:
        if self.veiculo_repo.buscar_placa(veiculo_model.placa):
            raise ValueError(f"Já existe um veículo cadastrado com a placa {veiculo_model.placa}.")
        
        if not veiculo_model.cliente_id:
            raise ValueError("O ID do cliente não pode ser nulo.")

        veiculo_id = self.veiculo_repo.adicionar(veiculo_model)
        self.veiculo_repo.db.commit()
        return veiculo_id
    
    def buscar_por_placa(self, placa: str) -> Veiculo:
        veiculo = self.veiculo_repo.buscar_placa(placa)

        if not veiculo:
            raise ValueError(f"Não existe um veículo cadastrado com a placa {placa}.")
        
        return veiculo
    
    def veiculo_existe(self, placa: str) -> bool:
        try:
            self.buscar_por_placa(placa)
            return True
        
        except ValueError:
            return False
    
    def listar_veiculos(self) -> list[Veiculo]:
        return self.veiculo_repo.listar_todos()
    
    def transferir_proprietario(self, cliente_id: int, placa: str) -> None:
        self.veiculo_repo.transferir_proprietario(cliente_id, placa)
        self.veiculo_repo.db.commit()

    def listar_placas(self) -> list[str]:
        veiculos = self.listar_veiculos()

        return [v.placa for v in veiculos]