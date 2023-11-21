import csv
import json
import logging.config

from decimal import *
from dicttoxml import dicttoxml
from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql
from src.students_accommodation.logger import logging_config
from xml.dom.minidom import parseString


def get_procedure_name(argument: str) -> str:
    """ Receive right name for calling procedure.

    :param argument: argument from CLI with procedure name
    :return: string with procedure name for sql query
    """
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


def write_in_file(file_format: str, data: list, procedure_name: str, header_fields: list) -> None:
    """ Write receiving data into necessary file format.

    :param file_format: argument from CLI with choosing file format (for saving data)
    :param data: list with scrapped data from database
    :param procedure_name: argument from CLI with procedure name for creating file name
    :param header_fields: list with header arguments
    """
    match file_format:

        case 'json':
            with open(f'./output/{procedure_name}_data.{file_format}', 'w') as file:
                json.dump(data, file, indent=4)

        case 'xml':
            xml = dicttoxml(data)
            parsed_xml = parseString(xml)
            with open(f'./output/{procedure_name}_data.{file_format}', 'w') as file_name:
                print(parsed_xml.toprettyxml(), file=file_name)

        case 'csv':
            with open(f'./output/{procedure_name}_data.{file_format}', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header_fields, delimiter=';')
                writer.writeheader()
                writer.writerows(data)

        case _:
            print('Wrong file format when trying write into file.')


def get_results_from_db(db_config: dict, procedures_args: dict, file_format: str) -> None:
    """ Scrap data from database.

    Call procedure for getting results and send data to write it into file.

    :param db_config: configurations for db connection
    :param procedures_args: dictionary with CLI procedures arguments
    :param file_format: argument from CLI with choosing file format (for saving data)
    """
    for key, value in procedures_args.items():
        if value:
            with connect_to_mysql(db_config) as cnx:

                if not cnx or not cnx.is_connected():
                    print("Couldn't connect")
                else:
                    print(
                        f"Connected to database: {db_config['database']}")  # test load func, shouldn’t show up in prod

                    with cnx.cursor() as cursor:
                        procedure_name = get_procedure_name(key)
                        cursor.callproc(procedure_name)  # calling procedures

                        list_results = []  # original formats receiving results
                        final_data_list = []  # changed formats receiving results
                        for result in cursor.stored_results():
                            list_result_keys = []

                            for field in result.description:
                                list_result_keys.append(field[0])  # get column name from description

                            data = result.fetchall()  # scrap data one time

                            for item in data:
                                list_results.append(dict(zip(list_result_keys, item)))

                            for list_item in list_results:
                                new_dict = {}
                                for d_key, d_value in list_item.items():

                                    if isinstance(d_value, Decimal):
                                        new_dict[d_key] = float(d_value)
                                    else:
                                        new_dict[d_key] = d_value

                                final_data_list.append(new_dict)

                            write_in_file(file_format, final_data_list, procedure_name, list_result_keys)

                print('Scrap data from DB.')
