from src.accommodation_students_by_rooms.cmd_line_parser import modify_parser
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser = modify_parser(parser)
