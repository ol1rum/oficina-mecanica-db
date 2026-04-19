from functools import wraps
from .quest_base import FluxoCancelado
from ..utils import formatar_moeda, limpar_cpf

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