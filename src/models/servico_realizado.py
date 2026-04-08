from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal



@dataclass
class ServicoRealizado:
    valor_cobrado: Decimal
    os_id: int
    servico_id: int
    mecanico_id: int
    data_execucao: datetime | None = None
    id: int | None = None