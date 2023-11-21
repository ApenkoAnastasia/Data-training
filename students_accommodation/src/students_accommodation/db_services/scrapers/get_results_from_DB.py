import json

from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql
from decimal import *
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

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


def write_in_file(file_format: str, data: list, procedure_name: str):
    match file_format:

        case 'json':
            with open(f'./output/{procedure_name}_data.{file_format}', 'w') as file:
                json.dump(data, file, indent=4)

        case 'xml':
            xml = dicttoxml(data)
            parsed_xml = parseString(xml)
            with open(f'./output/{procedure_name}_data.{file_format}', 'w') as file_name:
                print(parsed_xml.toprettyxml(), file=file_name)
            # print(parsed_xml.toprettyxml())

        case 'csv':
            pass

        case _:
            print('Wrong file format when trying write into file.')


def get_results_from_db(db_config: dict, procedures_args: dict, file_format: str):
    print(procedures_args)
    print(file_format)
    for key, value in procedures_args.items():
        if value:
            with connect_to_mysql(db_config) as cnx:

                if not cnx or not cnx.is_connected():
                    print('Could not connect')
                else:
                    print(f"Connected to database: {db_config['database']}")  # test load func, shouldn’t show up in prod

                    with cnx.cursor() as cursor:
                        procedure_name = get_procedure_name(key)
                        cursor.callproc(procedure_name)  # calling procedures

                        list_results = []
                        new_list = []
                        for result in cursor.stored_results():
                            list_result_keys = []

                            for field in result.description:
                                list_result_keys.append(field[0]) # get column name from description

                            data = result.fetchall()

                            for item in data:
                                list_results.append(dict(zip(list_result_keys, item)))

                            for list_item in list_results:
                                new_dict = {}
                                for d_key, d_value in list_item.items():

                                    if isinstance(d_value, Decimal):
                                        new_dict[d_key] = float(d_value)
                                    else:
                                        new_dict[d_key] = d_value

                                new_list.append(new_dict)

                            write_in_file(file_format, new_list, procedure_name)
                            # print(new_list)

                print('Scrap data from DB.')
