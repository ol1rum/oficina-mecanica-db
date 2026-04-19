from dataclasses import dataclass
from datetime import date


@dataclass
class Cliente:
    cpf: str
    data_nasc: date
    nome: str
    endereco: str
    id: int | None = None