import logging

from src.students_accommodation.models.entities import Room, Student
from src.students_accommodation.parsers.file_parser import *
from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql

logger = logging.getLogger('studentsLog')


def get_sql_query(table_name: str):
    """ Receive string of SQL query for inserting info into tables.

    :param table_name: string with name of chosen table
    :return: string with SQL query
    """
    match table_name:

        case 'room_list':
            return "INSERT INTO room_list (room_id, room_name) VALUES (%s, %s);"

        case 'students_list':
            return ("INSERT INTO students_list (birthday, student_id, student_name, room_id, sex) "
                    "VALUES (%s, %s, %s, %s, %s);")

        case _ as err:
            logger.error('Wrong table name when trying get sql query.', err)


def get_object(table_name: str, item: dict):
    """ Transform dictionary with read data into class object type.

    :param table_name: string with name of chosen table
    :param item: dictionary with read data
    :return: transformed data to object
    """
    match table_name:

        case 'room_list':
            item_as_obj = Room(**item)
            return item_as_obj

        case 'students_list':
            item_as_obj = Student(**item)
            return item_as_obj

        case _ as err:
            logger.error('Wrong table name when trying transform to class object.', err)


def get_processed_data(file_path: str, input_files_format: str = 'json') -> list:
    """ Receive processed data matching input file format.

    Calling methods for processing data in chosen format.

    :param file_path: string with path to the parsing file
    :param input_files_format:  type of input file format (default=json)
    :return: list with parsed data from input file
    """
    match input_files_format:

        case 'json':
            parsed_json = json_parser(file_path)
            return parsed_json

        case 'xml':
            parsed_xml = xml_parser(file_path)
            return parsed_xml

        case 'csv':
            parsed_csv = csv_parser(file_path)
            return parsed_csv

        case _ as err:
            logger.error('Wrong reading file format when trying parse file.', err)


def get_db_loader_type(config: dict, table_name: str, parsed_data: list, db_type: str = 'MySQL') -> None:
    """ Calling methods for loading data in chosen DB.

    :param config: configurations for connection to chosen DB
    :param table_name: string with name of chosen table
    :param parsed_data: list with parsed data from input file
    :param db_type: string with chosen DB from CLI
    """
    match db_type:

        case 'MySQL':
            load_to_mysql(config, table_name, parsed_data)

        case 'Postgres':
            load_to_postgres(config)

        case 'MongoDB':
            pass

        case _ as err:
            logger.error('Wrong DB type when trying choose loader.', err)


def load_to_mysql(config: dict, table_name: str, data_to_be_inserted: list) -> None:
    """ Insert parsed data to MySQL DB.

    :param config: configurations for connection to MySQL DB
    :param table_name: string with name of chosen table
    :param data_to_be_inserted: list with parsed data from input file
    """
    cnx = connect_to_mysql(config)

    if not cnx or not cnx.is_connected():
        logger.info("Could not connect")
    else:
        logger.info(f"Connected to database: {config['database']}")

        with cnx.cursor() as cursor:

            for item in data_to_be_inserted:
                sql = get_sql_query(table_name)

                item_as_obj = get_object(table_name, item)
                list_obj = item_as_obj.get_list_attributes()

                cursor.execute(sql, list_obj)

                cnx.commit()
        logger.info('Copied data to MySQL DB.')
        cursor.close()
        cnx.close()


def load_to_postgres(config: dict) -> None:
    """

    :param config: configurations for connection to Postgres DB
    """
    logger.info('Started load data to PstgreSQL DB.')


def full_load(order_paths: list, order_tables: list, config: dict) -> None:
    """ Full initial load to DB.

    :param order_paths: list with paths to files
    :param order_tables: list with names of tables
    :param config: configurations for connection to chosen DB
    """
    logger.info('Started full load.')

    for i in range(len(order_paths)):
        parsed_data = get_processed_data(order_paths[i])
        get_db_loader_type(config, order_tables[i], parsed_data)


def incremental_load(config: dict) -> None:
    """ Incremental load to DB.

    :param config: configurations for connection to chosen DB
    """
    logger.info('Started incremental load.')
