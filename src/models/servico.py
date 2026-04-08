from dataclasses import dataclass
from datetime import date
from decimal import Decimal



@dataclass
class Servico:
    descricao: str
    preco: Decimal
    disponivel: bool = True
    id: int | None = None