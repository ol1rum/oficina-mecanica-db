from dataclasses import dataclass


@dataclass
class Veiculo:
    placa: str
    marca: str
    modelo: str
    cliente_id: int
    cor: str | None = None
    ano: int | None = None
    id: int | None = None