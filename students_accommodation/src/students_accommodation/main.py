import argparse
import logging.config

from src.students_accommodation.cmd_line_parser import modify_parser
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
