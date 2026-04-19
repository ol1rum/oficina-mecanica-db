from dataclasses import dataclass
from datetime import datetime


@dataclass
class OrdemServico:
    quilometragem_abertura: int
    veiculo_id: int
    cliente_id: int
    observacoes: str | None = None
    numero_os: str | None = None
    status: str = "EM EXECUÇÃO"  # EM EXECUÇÃO | FINALIZADO | CANCELADO
    data_hora_fechamento: datetime | None = None
    data_hora_abertura: datetime | None = None
    id: int | None = None

@dataclass
class OSDetalhada:
    numero_os: str
    cliente_nome: str
    cliente_cpf: str
    veiculo_placa: str
    quilometragem_abertura: int
    data_hora_abertura: datetime
    status: str
    observacoes: str | None = None
    data_hora_fechamento: datetime | None = None