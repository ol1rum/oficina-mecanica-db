from ..models.cliente import Cliente
from .base_repo import BaseRepository
from ..database import DatabaseManager


class ClienteRepository(BaseRepository):

    def __init__(self, db_manager: DatabaseManager) -> None:
        super().__init__(db_manager, "cliente")

    def adicionar(self, cliente: Cliente) -> int:
        return self.exec_sql(
            "adicionar.sql",
            (
                cliente.cpf,
                cliente.data_nasc,
                cliente.nome,
                cliente.endereco
            )
        )

    def listar_todos(self) -> list[Cliente]:
        res: list[dict] = self.db.consultar(self.path, "listar_todos.sql")

        lista_clientes: list = [Cliente(**res) for res in res]
        return lista_clientes


    def buscar_cpf(self, cpf: str) -> Cliente | None:
        busca: list[dict] = self.db.consultar(self.path, "listar_por_cpf.sql", (cpf,))

        return Cliente(**busca[0]) if busca else None

    def buscar_id(self, id: int) -> Cliente | None:
        busca: list[dict] = self.db.consultar(self.path, "buscar_id.sql", (id,))

        return Cliente(**busca[0]) if busca else None