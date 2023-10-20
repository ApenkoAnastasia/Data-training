from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql


def load_to_mysql(config: dict):
    """

    :param config: dict
    """
    cnx = connect_to_mysql(config)
    if cnx and cnx.is_connected():
        print(f"Connected to database: {config['database']}")

        with cnx.cursor() as cursor:

            result = cursor.execute("SELECT * FROM students_list LIMIT 5")

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        cnx.close()

    else:

        print("Could not connect")


def load_to_postgres(config: dict):
    pass
