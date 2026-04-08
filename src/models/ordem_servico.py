from dataclasses import dataclass
from datetime import datetime



@dataclass
class OrdemServico:
    numero_os: str
    quilometragem_abertura: int
    veiculo_id: int
    cliente_id: int
    observacoes: str | None = None
    status: str = "EM EXECUÇÃO"  # EM EXECUÇÃO | FINALIZADO | CANCELADO
    data_hora_fechamento: datetime | None = None
    data_hora_abertura: datetime | None = None
    id: int | None = None