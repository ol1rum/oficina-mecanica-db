from prompt_toolkit.document import Document
from questionary import Validator, ValidationError
from datetime import datetime
from typing import Callable, Any
import re

class ListaExistentesValidator(Validator):
    def __init__(self, lista_opcoes: list, msg_erro: str = "Opção inválida. Escolha da lista.") -> None:
        self.msg_erro = msg_erro
        self.lista_opcoes = lista_opcoes

    def validate(self, document: Document) -> None:
        if document.text not in self.lista_opcoes:
            raise ValidationError(message=self.msg_erro, cursor_position=len(document.text))

class DataValidator(Validator):
    def validate(self, document: Document) -> None:
        if not document.text: # Permite vazio se necessário, ou adicione check
            return
        
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", document.text):
            raise ValidationError(
                message="Formato inválido. Use DD/MM/AAAA (ex: 15/04/2026)",
                cursor_position=len(document.text)
            )
        try:
            datetime.strptime(document.text, "%d/%m/%Y")
        except ValueError:
            raise ValidationError(
                message="Data inexistente no calendário.",
                cursor_position=len(document.text)
            )

class NumeroValidator(Validator):
    def __init__(self, tamanho: int | None = None, decimal: bool = False, msg_erro: str = "Digite apenas números."):
        self.tamanho = tamanho
        self.msg_erro = msg_erro
        self.decimal = decimal

    def validate(self, document: Document) -> None:
        try:
            if self.decimal:
                float(document.text)
            else:
                int(document.text)

        except ValueError:
            raise ValidationError(message=self.msg_erro, cursor_position=len(document.text))
        
        if self.tamanho and len(document.text) != self.tamanho:
            raise ValidationError(
                message=f"Deve ter exatamente {self.tamanho} dígitos.",
                cursor_position=len(document.text)
            )

class NovoCPFValidator(Validator):
    def __init__(
            self,
            cpf_existe: Callable[[str], Any],
            msg_erro: str = "CPF já cadastrado."
    ) -> None:
        
        self.busca = cpf_existe
        self.msg_erro = msg_erro

    def validate(self, document: Document) -> None:
        if not document.text.isdigit() or len(document.text) != 11:
            raise ValidationError(message="O CPF deve conter exatamente 11 dígitos.", cursor_position=len(document.text))
        
        if self.busca(document.text):
            raise ValidationError(message=self.msg_erro, cursor_position=len(document.text))
        
class NovoValorStr(Validator):
    def __init__(self, lista_str: list[str], msg_erro: str = "Valor já existente") -> None:
        self.msg_erro = msg_erro
        self.lista_str = [valor.lower() for valor in lista_str]

    def validate(self, document: Document) -> None:
        if any(document.text.lower() == string for string in self.lista_str):
            raise ValidationError(message=self.msg_erro, cursor_position=len(document.text))