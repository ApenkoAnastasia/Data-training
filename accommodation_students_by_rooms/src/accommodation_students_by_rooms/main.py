import argparse


Console_Output = 'console'
File_Output = 'file'
Delimiter = ', '
def modify_parser(parser):
    """Prepare arguments.

    Function for preparation of Namespace arguments.

    Keyword arguments:
    parser -- get an ArgumentParser object

    """
    parser.add_argument('--list_count',
                        type=str,
                        help='List of rooms and number of students in each of them.'
                             'syntax: [--list_count "string"]')

    parser.add_argument('--min_avg',
                        type=str,
                        help='5 rooms where the average age of students is the smallest.'
                             'syntax: [--min_avg "string"]')

    parser.add_argument('--max_avg',
                        type=str,
                        help='5 rooms with the biggest age difference between students.'
                             'syntax: [--max_avg "string"]')

    parser.add_argument('--list_of_mix',
                        type=str,
                        help='List of rooms where mixed-sex students live.'
                             'syntax: [--list_of_mix "string"]')

    parser.add_argument('--disp',
                        choices=[Console_Output, File_Output],
                        default=Console_Output,
                        type=str,
                        help='set the way of displaying information.')

    return parser


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser = modify_parser(parser)

