import argparse
import logging.config

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

    st_path, rm_path, db_name = args.students_path, args.rooms_path, args.database

    # add_path_config(st_path, rm_path)  # Add cli paths to settings.ini
    # delimiter = get_format_config()[0] # Get .ini configs

    db_config = get_db_config(db_name)

    table1, table2 = get_table_names()

    order_paths = [rm_path, st_path]
    order_tables = [table1, table2]

    full_load(order_paths, order_tables, db_config)


if __name__ == "__main__":
    main()
