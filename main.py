from database.connection import get_connection
from database.queries import buscar_produtos

def main():
    print("🚀 Iniciando automação de banco...")

    conn = get_connection()

    if not conn:
        print("Encerrando aplicação.")
        return

    try:
        resultados = buscar_produtos(conn)

        print("\n📋 Tabelas encontradas:")
        print("=" * 40)

        for linha in resultados:
            print(f"- {linha[0]}")

        print("=" * 40)

    except Exception as e:
        print(f"Erro durante execução: {e}")

    finally:
        conn.close()
        print("🔒 Conexão encerrada.")

if __name__ == "__main__":
    main()