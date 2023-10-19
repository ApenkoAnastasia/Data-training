import argparse
import logging.config
import cli_parser
import config_parser
import entities
import logging_config

from file_parser import json_parser


logger = logging.getLogger(__name__)


def main():
    logging.config.dictConfig(logging_config.LOGGING_CONFIG)

    parser = argparse.ArgumentParser(prog="main.py",
                                     description="Help to get information about students accommodation by rooms.",
                                     epilog="For more details go to the README.md.")

    parser = cli_parser.modify_parser(parser)

    args = parser.parse_args()

    st_path, rm_path = args.students_path, args.rooms_path

    # config_parser.add_path_config(st_path, rm_path)  # Add cli paths to settings.ini

    # config_parser.get_db_config()

    # delimiter = config_parser.get_format_config()[0]

    parsed_json = json_parser(st_path)

    # for item in parsed_json:        # test class, shouldn’t show up in prod
    #     room_obj = entities.Room(**item)
    #     print(room_obj)

    print(parsed_json)
    for item in parsed_json:  # test class, shouldn’t show up in prod
        student_obj = entities.Student(**item)
        print(student_obj)


if __name__ == "__main__":
    main()
