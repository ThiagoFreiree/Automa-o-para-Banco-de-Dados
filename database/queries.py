def buscar_produtos(conn):
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """

    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
