from pathlib import Path

CAMINHO_ROOT = Path(__file__).resolve().parent.parent
CAMINHO_SQL = CAMINHO_ROOT / 'sql'
CAMINHO_SQL_QUERIES = CAMINHO_SQL / 'queries'
CAMINHO_SQL_COMMANDS = CAMINHO_SQL / 'commands'

if __name__ == '__main__':
    print(CAMINHO_ROOT)
    print(CAMINHO_SQL)
    print(CAMINHO_SQL_QUERIES)
    print(CAMINHO_SQL_COMMANDS)