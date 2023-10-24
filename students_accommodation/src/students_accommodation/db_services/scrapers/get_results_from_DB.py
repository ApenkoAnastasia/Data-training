from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql


def get_procedure_name(argument: str):
    match argument:

        case 'list_count':
            return 'get_amount_of_students_in_rooms'

        case 'min_avg':
            return 'get_min_average_age'

        case 'max_avg':
            return 'get_max_average_age'

        case 'list_of_mix':
            return 'get_rooms_with_different_sex'

        case _:
            print('Wrong argument when trying call procedure.')


def write_in_file(file_format: str):
    match file_format:

        case 'json':
            return "INSERT INTO room_list (room_id, room_name) VALUES (%s, %s);"

        case 'xml':
            return ("INSERT INTO students_list (birthday, student_id, student_name, room_id, sex) "
                    "VALUES (%s, %s, %s, %s, %s);")

        case 'csv':
            return ""

        case _:
            print('Wrong file format when trying write into file.')


def get_results_from_db(db_config: dict, procedures_args: dict, file_format: str):
    print(procedures_args)
    print(file_format)
    for key, value in procedures_args.items():
        if value:
            with connect_to_mysql(db_config) as cnx:

                if not cnx or not cnx.is_connected():
                    print("Could not connect")
                else:
                    print(f"Connected to database: {db_config['database']}")  # test load func, shouldn’t show up in prod

                    with cnx.cursor() as cursor:
                        p_name = get_procedure_name(key)
                        cursor.callproc(p_name)
                        # for col_id in cursor.stored_results():
                        #     columnsProperties = (col_id.description)
                        #     print([column[0] for column in columnsProperties])
                        for result in cursor.stored_results():
                            dict_res = {}
                            print(result.description)
                            print(result.fetchall())

                print('Scrap data from DB.')
