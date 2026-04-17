import questionary
from typing import Any
from .validadores import ListaExistentesValidator, DataValidator, NumeroValidator
from datetime import date

class FluxoCancelado(Exception):
    """Exceção para interromper o fluxo de perguntas quando o usuário cancela (None ou Ctrl+C)."""
    pass

def perguntar(prompt_obj: Any) -> Any:
    """
    Executa o prompt e valida se a resposta é None.
    Lança FluxoCancelado se o usuário cancelar.
    """
    # Para o autocomplete do prompt_toolkit/questionary, 
    # as vezes o objeto retornado por ask() pode ser None se cancelado.
    resposta = prompt_obj.ask()
    if resposta is None:
        raise FluxoCancelado()
    return resposta

def pausar(mensagem: str = "Pressione qualquer tecla para continuar...") -> None:
    """
    Faz uma pausa no sistema e aguarda qualquer interação do usuário.
    """
    questionary.press_any_key_to_continue(
        message=mensagem,
    ).ask()

def menu(mensagem: str, opcoes: dict[str, str]) -> str:
    """Exibe um menu de seleção e retorna a chave escolhida."""
    lista_choice = [
        questionary.Choice(title=titulo, value=chave) for chave, titulo in opcoes.items()
    ]

    prompt = questionary.select(
        mensagem,
        choices=lista_choice,
        use_shortcuts=True,
        pointer="🔹",
        instruction="(use as setas ou teclas de atalho para navegar)"
    )
    
    return perguntar(prompt)

def buscar_na_lista(msg: str, lista_choices: list[str]) -> str:
    """Autocomplete com validação obrigatória de item da lista."""
    prompt = questionary.autocomplete(
        msg,
        choices=lista_choices,
        match_middle=True,
        ignore_case=True,
        validate=ListaExistentesValidator(lista_choices)
    )
    
    return perguntar(prompt)

def texto(msg: str, default: str = "", validate: Any = None) -> str:
    """Solicita uma entrada de texto livre."""
    prompt = questionary.text(
        msg,
        default=default,
        validate=validate
    )
    
    return perguntar(prompt)

def numero(msg: str, tamanho: int  | None = None, decimal: bool = False, default: str = "") -> str:
    """Solicita apenas números."""
    prompt = questionary.text(
        msg,
        default=default,
        validate=NumeroValidator(tamanho=tamanho, decimal=decimal)
    )
    return perguntar(prompt)

def data(msg: str, default: str = "") -> str:
    """Solicita uma data válida no formato DD/MM/AAAA."""
    if not default:
        default = date.today().strftime("%d/%m/%Y")

    prompt = questionary.text(
        msg,
        instruction="(DD/MM/AAAA)",
        validate=DataValidator(),
        default=default
    )
    return perguntar(prompt)

def confirmar(msg: str, default: bool = True) -> bool:
    """Pergunta de Sim/Não."""
    prompt = questionary.confirm(
        msg,
        default=default,
        instruction="(enter/n)"
    )
    
    return perguntar(prompt)
