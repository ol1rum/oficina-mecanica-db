from src.cli import OficinaCLI
from src.database import DatabaseManager


class Main():

    def __init__(self) -> None:
        pass # O __init__ do DatabaseManager já carrega o .env

    def iniciar(self):
        db_manager = DatabaseManager()
        cli = OficinaCLI(db_manager)
        cli.iniciar()

if __name__ == '__main__':
    main = Main()
    main.iniciar()