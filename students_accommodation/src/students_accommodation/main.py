import argparse
import logging.config

from src.students_accommodation.cli_parser import modify_parser
from src.students_accommodation.config_parser import *
from src.students_accommodation.file_parser import *
from src.students_accommodation.entities import *
from src.students_accommodation.logging_config import LOGGING_CONFIG

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.config.dictConfig(LOGGING_CONFIG)

    parser = argparse.ArgumentParser(prog="main.py",
                                     description="Help to get information about students accommodation by rooms.",
                                     epilog="For more details go to the README.md.")

    parser = modify_parser(parser)

    args = parser.parse_args()

    st_path, rm_path = args.students_path, args.rooms_path

    # add_path_config(st_path, rm_path)  # Add cli paths to settings.ini

    # get_db_config()

    # delimiter = get_format_config()[0]

    parsed_json = json_parser(rm_path)

    print(type(parsed_json))
    for item in parsed_json:
        room_obj = Room(**item)
        print(room_obj)
