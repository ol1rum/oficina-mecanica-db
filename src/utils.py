from pathlib import Path
import pandas as pd
from dataclasses import asdict

CAMINHO_ROOT = Path(__file__).resolve().parent.parent
CAMINHO_SQL = CAMINHO_ROOT / 'sql'

from decimal import Decimal

def objeto_para_dataframe(lista_obj: list):
    dados = [asdict(obj) for obj in lista_obj]
    return pd.DataFrame(dados)

def validar_cpf(cpf: str) -> bool:
    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

# Converter float para formato de dinheiro
def formatar_moeda(valor: float | Decimal | int) -> str:
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def limpar_cpf(cpf: str) -> str:
    return cpf.replace(".", "").replace("-", "").replace("(", "").replace(")", "").strip()
