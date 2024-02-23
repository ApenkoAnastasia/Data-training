import argparse
import logging.config

from src.students_accommodation.parsers.cli_parser import modify_parser
from src.students_accommodation.parsers.config_parser import *
from src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql
from src.students_accommodation.db_services.scrapers.get_results_from_DB import get_results_from_db
from src.students_accommodation.parsers.file_parser import json_parser
from src.students_accommodation.db_services.loaders.load_to_db import load_to_mysql, full_load
from src.students_accommodation.models.entities import *

LOG_CONFIG_PATH = './properties/logging.conf'


def test_connection_from_container(config: dict):
    try:
        cnx = connect_to_mysql(config)
        cnx.close()
    except (AttributeError, IOError) as err:
        logger.error("Failed to connect, exiting without a connection. Can't close cursor: %s", err, exc_info=True)


def main():
    # create Logger
    logging.config.fileConfig(LOG_CONFIG_PATH)
    logger = logging.getLogger('studentsLog')

    # parse arguments from CLI
    parser = argparse.ArgumentParser(prog='python3 -m src.app.main',
                                     description='CLI application to get information about students accommodation by rooms.',
                                     epilog='For more details go to the README.md file.')
    parser = modify_parser(parser)
    args = parser.parse_args()

    # file check
    stud_path = args.students_path
    room_path = args.rooms_path
    try:
        with open(args.students_path, 'r') as file:
            logger.info(f"File {file.name} exists.")
    except FileNotFoundError as err:
        logger.warning("Cannot find file with students path %s.", err, exc_info=True)
        stud_path = get_students_path()
        logger.info(f"Replace file path for such: {stud_path}.")

    try:
        with open(args.rooms_path, 'r') as file:
            logger.info(f"File {file.name} exists.")
    except FileNotFoundError as err:
        logger.warning("Cannot find file with rooms path %s.", err, exc_info=True)
        room_path = get_rooms_path()
        logger.info(f"Replace file path for such: {room_path}.")

    main_args = {'st_path': stud_path, 'rm_path': room_path,
                 'db_name': args.database, 'file_format': args.format}

    procedures_args = {'list_count': args.list_count, 'min_avg': args.min_avg,
                       'max_avg': args.max_avg, 'list_of_mix': args.list_of_mix}

    # add_path_config(main_args['st_path'], main_args['rm_path'])  # Add cli paths to settings.ini
    # delimiter = get_format_config()[0]  # Get .ini configs

    # parse config file
    db_config = get_db_config(main_args['db_name'])

    table1, table2 = get_table_names()

    test_connection_from_container(db_config)

    order_paths = [main_args['rm_path'], main_args['st_path']]
    order_tables = [table1, table2]

    # initial load to chosen DB
    if args.initial_load:
        full_load(order_paths, order_tables, db_config)

    # receive processed data from DB and saving it into file
    get_results_from_db(db_config, procedures_args, main_args['file_format'])


if __name__ == "__main__":
    main()
    logger.info("Program finished. ***********************")
