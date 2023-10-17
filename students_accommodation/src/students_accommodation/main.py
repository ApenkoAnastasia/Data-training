import argparse
from src.students_accommodation.cmd_line_parser import modify_parser

if __name__ == "__main__":
    """Entry point."""

    parser = argparse.ArgumentParser(prog="main.py",
                                     description="Help to get information about students accommodation by rooms.",
                                     epilog="For more details go to the README.md.")

    parser = modify_parser(parser)

    args = parser.parse_args()
