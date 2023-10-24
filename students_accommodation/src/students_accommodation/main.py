import argparse
import logging.config

from src.students_accommodation.db_services.scrapers.get_results_from_DB import get_results_from_db
from src.students_accommodation.parsers.config_parser import *
from src.students_accommodation.parsers.file_parser import json_parser
from src.students_accommodation.parsers.cli_parser import modify_parser
from src.students_accommodation.logger import logging_config
from src.students_accommodation.db_services.loaders.load_to_db import load_to_mysql, full_load
from src.students_accommodation.models.entities import *

logger = logging.getLogger(__name__)


def main():
    logging.config.dictConfig(logging_config.LOGGING_CONFIG)

    parser = argparse.ArgumentParser(prog="main.py",
                                     description="Help to get information about students accommodation by rooms.",
                                     epilog="For more details go to the README.md.")
    parser = modify_parser(parser)
    args = parser.parse_args()

    main_args = {'st_path': args.students_path, 'rm_path': args.rooms_path,
                 'db_name': args.database, 'file_format': args.format}

    procedures_args = {'list_count': args.list_count, 'min_avg': args.min_avg,
                       'max_avg': args.max_avg, 'list_of_mix': args.list_of_mix}

    # add_path_config(main_args['st_path'], main_args['rm_path'])  # Add cli paths to settings.ini
    # delimiter = get_format_config()[0] # Get .ini configs

    db_config = get_db_config(main_args['db_name'])

    table1, table2 = get_table_names()

    order_paths = [main_args['rm_path'], main_args['st_path']]
    order_tables = [table1, table2]

    # full_load(order_paths, order_tables, db_config)

    get_results_from_db(db_config, procedures_args, main_args['file_format'])


if __name__ == "__main__":
    main()
