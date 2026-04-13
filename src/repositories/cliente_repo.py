from ..models.cliente import Cliente
from .base_repo import BaseRepository



class ClienteRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__("cliente")

    def adicionar(self, cliente: Cliente) -> int:
        return self.execSql(
            "adicionar.sql",
            (
                cliente.cpf,
                cliente.data_nasc,
                cliente.nome,
                cliente.endereco
            ),
        )

    def listarTodos(self) -> list[Cliente]:
        res: list[dict] = self.db.consultar("listar_todos.sql")

        lista_clientes: list = [Cliente(**res) for res in res]
        return lista_clientes


    def buscarCpf(self, cpf: str) -> Cliente | None:
        busca: list[dict] = self.db.consultar("listar_por_cpf.sql", (cpf,))

        return Cliente(**busca[0]) if busca else None
