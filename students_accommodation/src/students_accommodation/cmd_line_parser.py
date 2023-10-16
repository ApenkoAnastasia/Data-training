LIST_OF_FORMATS = ['json', 'xml', 'csv']


def modify_parser(parser):
    """Prepare arguments.

    Function for preparation of Namespace arguments.

    Keyword arguments:
    parser -- get an ArgumentParser object

    """
    parser.add_argument('--students_path', '-sp',
                        type=str,
                        required=True,
                        help='Path to students file.')

    parser.add_argument('--rooms_path', '-rp',
                        type=str,
                        required=True,
                        help='Path to rooms file.')

    parser.add_argument('--format', '-f',
                        choices=LIST_OF_FORMATS,
                        default=LIST_OF_FORMATS[0],
                        type=str,
                        help='Choose in which format to save the information. Default format - json.')

    parser.add_argument('--list_count', '-lc',
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help='List of rooms and number of students in each of them.')

    parser.add_argument('--min_avg',
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help='5 rooms where the average age of students is the smallest.')

    parser.add_argument('--max_avg',
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help='5 rooms with the biggest age difference between students.')

    parser.add_argument('--list_of_mix', '-lm',
                        type=int,
                        default=0,
                        choices=[0, 1],
                        help='List of rooms where mixed-sex students live.')

    return parser
