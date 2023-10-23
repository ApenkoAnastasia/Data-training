from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql
from src.students_accommodation.models.entities import Room, Student
from src.students_accommodation.parsers.file_parser import json_parser


def get_sql_query(table_name: str):

    match table_name:

        case 'room_list':
            return "INSERT INTO room_list (room_id, room_name) VALUES (%s, %s);"

        case 'students_list':
            return ("INSERT INTO students_list (birthday, student_id, student_name, room_id, sex) "
                    "VALUES (%s, %s, %s, %s, %s);")

        case _:
            print('Wrong table name when trying get sql query.')


def get_object(table_name: str, item: dict):

    match table_name:

        case 'room_list':
            item_as_obj = Room(**item)
            return item_as_obj

        case 'students_list':
            item_as_obj = Student(**item)
            return item_as_obj

        case _:
            print('Wrong table name when trying transform to class object.')


def load_to_mysql(config: dict, table_name: str, data_to_be_inserted: list):
    """

    :param data_to_be_inserted:
    :param table_name:
    :param config: dict
    """
    cnx = connect_to_mysql(config)

    if not cnx or not cnx.is_connected():
        print("Could not connect")
    else:

        print(f"Connected to database: {config['database']}")  # test load func, shouldn’t show up in prod

        with cnx.cursor() as cursor:

            for item in data_to_be_inserted:
                sql = get_sql_query(table_name)

                item_as_obj = get_object(table_name, item)
                list_obj = item_as_obj.get_list_attributes()

                cursor.execute(sql, list_obj)
                # emp_no = cursor.lastrowid  # get id of row, shouldn’t show up in prod

                cnx.commit()
                # print(cursor.rowcount, " rows got inserted. ")
            # print(emp_no)
        cursor.close()
        cnx.close()


def full_load(order_paths: list, order_tables: list, config: dict):
    for i in range(len(order_paths)):
        parsed_json = json_parser(order_paths[i])
        load_to_mysql(config, order_tables[i], parsed_json)


def load_to_postgres(config: dict):
    pass
