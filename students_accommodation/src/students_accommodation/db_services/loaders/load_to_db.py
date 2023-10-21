from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql
from datetime import datetime


def get_sql_query(table_name: str):
    print(table_name)
    match table_name:

        case 'room_list':
            return "INSERT INTO room_list (room_id, room_name) VALUES (%s, %s)"

        case 'students_list':
            return ("INSERT INTO students_list (student_id, student_name, birthday, sex, room_id) "
                    "VALUES (%s, %s, %s, %s, %s)")

        case _:
            print('Wrong table name.')


def load_to_mysql(config: dict, table_name: str):
    """

    :param table_name:
    :param config: dict
    """
    cnx = connect_to_mysql(config)
    if cnx and cnx.is_connected():
        print(f"Connected to database: {config['database']}")

        with cnx.cursor() as cursor:

            # result = cursor.execute(f"SELECT * FROM {table_name}")
            #
            # rows = cursor.fetchall()
            #
            # for row in rows:
            #     print(row)

            data = ((85, 'Koul Jameson', datetime.strptime("1990-01-14T00:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"), 'M', 28),
                    (86, 'Jane Jameson', datetime.strptime("1990-01-14T00:00:00.000000", "%Y-%m-%dT%H:%M:%S.%f"), 'F', 81))
            # data = ((81, 'Room #81'), (53, 'Room #53'))

            for item in data:
                sql = get_sql_query(table_name)
                print(sql)

                cursor.execute(sql, item)
                emp_no = cursor.lastrowid

                cnx.commit()
                print(cursor.rowcount, " rows got inserted. ")
            print(emp_no)
        cursor.close()

        cnx.close()

    else:

        print("Could not connect")


def load_to_postgres(config: dict):
    pass
