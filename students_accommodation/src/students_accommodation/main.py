import argparse
import logging.config

from src.students_accommodation.cli_parser import modify_parser
from src.students_accommodation.config_parser import *
from src.students_accommodation.logging_config import LOGGING_CONFIG

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    """Entry point."""

    logging.config.dictConfig(LOGGING_CONFIG)

    parser = argparse.ArgumentParser(prog="main.py",
                                     description="Help to get information about students accommodation by rooms.",
                                     epilog="For more details go to the README.md.")

    parser = modify_parser(parser)

    args = parser.parse_args()

    st_path, rm_path = args.students_path, args.rooms_path

    add_pathconfig(st_path, rm_path)

    get_dbconfig()

    # def get_config():
    #     '''Get data to connection.
    #
    #     Function that return dictionary of config data.
    #
    #     return -- dictionary of config data
    #
    #     '''
    #     config = {}
    #     with open('/Client/config.txt', 'r') as file:
    #         for line in file.readlines():
    #             data = line.strip().split(Delimiter)
    #             config[data[0]] = ''.join(data[1:])
    #
    #     return config
