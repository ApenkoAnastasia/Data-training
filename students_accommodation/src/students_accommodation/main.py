import argparse
import logging.config

from src.students_accommodation.parsers.config_parser import *
from src.students_accommodation.parsers.file_parser import json_parser
from src.students_accommodation.parsers.cli_parser import modify_parser
from src.students_accommodation.logger import logging_config
from src.students_accommodation.db_services.loaders.load_to_db import load_to_mysql
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

    db_config = get_db_config(db_name)
    print(db_config)

    table1, table2 = get_table_names()

    load_to_mysql(db_config, table2)

    # delimiter = get_format_config()[0] # Get .ini configs

    # parsed_json = json_parser(rm_path)
    #
    # for item in parsed_json:        # test class, shouldn’t show up in prod
    #     room_obj = Room(**item)
    #     print(room_obj)

    # print(parsed_json)
    # for item in parsed_json:  # test class, shouldn’t show up in prod
    #     student_obj = Student(**item)
    #     print(student_obj)


if __name__ == "__main__":
    main()
