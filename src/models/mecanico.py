from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Mecanico:
    cpf: str
    nome: str
    salario: Decimal
    data_contratacao: date | None = None
    data_demissao: date | None = None
    id: int | None = None
