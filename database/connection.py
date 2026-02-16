import psycopg2
from psycopg2 import OperationalError

from config.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def get_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        print("Conexao com o banco estabelecida com sucesso.")
        return connection
    except OperationalError as error:
        print(f"Erro ao conectar no banco: {error}")
        return None
