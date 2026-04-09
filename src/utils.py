from pathlib import Path

CAMINHO_ROOT = Path(__file__).resolve().parent.parent
CAMINHO_SQL = CAMINHO_ROOT / 'sql'

if __name__ == '__main__':
    print(CAMINHO_ROOT)
    print(CAMINHO_SQL)