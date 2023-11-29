LIST_OF_FORMATS = ['json', 'xml', 'csv']
TYPES_DB = ['MySQL', 'Postgres', 'MongoDB']


def modify_parser(parser):
    """ Method for parsing input arguments.

    :param parser: object with input arguments (ArgumentParser object)
    :return: object with parsed input arguments (ArgumentParser object)
    """
    parser.add_argument("--students_path", "-sp",
                        type=str,
                        required=True,
                        help="Path to students file.")

    parser.add_argument("--rooms_path", "-rp",
                        type=str,
                        required=True,
                        help="Path to rooms file.")

    parser.add_argument("--format", "-f",
                        choices=LIST_OF_FORMATS,
                        default=LIST_OF_FORMATS[0],
                        type=str,
                        help="Choose in which format to save the information. Default format - json.")

    parser.add_argument("--database", "-db",
                        choices=TYPES_DB,
                        default=TYPES_DB[0],
                        type=str,
                        help="Choose database to save the information. Default format - MySQL.")

    parser.add_argument("--list_count", "-lc",
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help="List of rooms and number of students in each of them.")

    parser.add_argument("--min_avg",
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help="5 rooms where the average age of students is the smallest.")

    parser.add_argument("--max_avg",
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help="5 rooms with the biggest age difference between students.")

    parser.add_argument("--list_of_mix", "-lm",
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help="List of rooms where mixed-sex students live.")

    return parser
