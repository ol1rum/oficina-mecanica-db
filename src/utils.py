from pathlib import Path
import pandas as pd
from dataclasses import asdict

CAMINHO_ROOT = Path(__file__).resolve().parent.parent
CAMINHO_SQL = CAMINHO_ROOT / 'sql'

def objetoParaDataframe(lista_obj: list):
    dados = [asdict(obj) for obj in lista_obj]
    return pd.DataFrame(dados)

def validarCpf(cpf: str) -> bool:
    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return False
    return True