from functools import wraps
from .quest_base import FluxoCancelado
from decimal import Decimal

def loop_menu(func):
    """
    Decorador que executa a função de menu em um loop infinito, 
    tratando a exceção FluxoCancelado automaticamente.
    O loop é interrompido se o menu retornar 'sair' ou 'voltar'.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                resultado = func(*args, **kwargs)
                
                if resultado in ("sair", "voltar"):
                    break
                    
            except FluxoCancelado:
                pass
                
    return wrapper

# Converter float para formato de dinheiro
def formatar_moeda(valor: float | Decimal | int) -> str:
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def limpar_cpf(cpf: str) -> str:
    return cpf.replace(".", "").replace("-", "").replace("(", "").replace(")", "").strip()