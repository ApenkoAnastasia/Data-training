LIST_OF_FORMATS = ['json', 'xml', 'csv']


def modify_parser(parser):
    """Prepare arguments.

    Function for preparation of Namespace arguments.

    Keyword arguments:
    parser -- get an ArgumentParser object

    """
    parser.add_argument('--students',
                        type=str,
                        help='Path to students file.'
                             'syntax: [--students "string"]')

    parser.add_argument('--rooms',
                        type=str,
                        help='Path to rooms file.'
                             'syntax: [--rooms "string"]')

    parser.add_argument('--format',
                        choices=LIST_OF_FORMATS,
                        default=LIST_OF_FORMATS[0],
                        type=str,
                        help='Choose in which format to save the information.'
                             'syntax: [--format "string"]')

    return parser
