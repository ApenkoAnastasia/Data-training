import configparser
import logging
from typing import Tuple

SETTINGS_PATH = './properties/settings.ini'
DB_CONFIGS = ['user', 'password', 'host', 'port', 'database']
logger = logging.getLogger('studentsLog')


def get_config():
    """ Receive config object

    :return: config object
    """
    config = configparser.ConfigParser()

    return config


def add_path_config(stud_path_cli: str, room_path_cli: str) -> None:
    """ Write path of input files into config doc.

    :param stud_path_cli: path to students file
    :param room_path_cli: path to room list file
    """
    config = get_config()

    config.add_section('CLI variables')
    config.set('CLI variables', 'students_path', stud_path_cli)
    config.set('CLI variables', 'rooms_path', room_path_cli)

    with open(SETTINGS_PATH, 'a') as config_file:
        config.write(config_file)


def get_db_config(db_name: str) -> dict:
    """  Receive configurations to DB connection from config doc.

    :param db_name: DB name from CLI
    :return: dictionary with configurations to connection
    """
    config = get_config()

    config.read(SETTINGS_PATH)

    db_config = {}

    for section in DB_CONFIGS:
        db_config[section] = config[db_name][section]

    db_config['allow_local_infile'] = True

    return db_config


def get_table_names() -> tuple[str, str]:
    """ Receive table names from DB.

    :return: tuple with table names
    """
    config = get_config()

    config.read(SETTINGS_PATH)

    return config['Tables']['table1'], config['Tables']['table2']


def get_format_config() -> tuple[str, str]:
    """ Receive formats for further transformations.

    :return: tuple with strings of formats
    """
    config = get_config()

    config.read(SETTINGS_PATH)

    delimiter = config['Formats']['delimiter']
    date_format = config['Formats']['date_format']

    return delimiter, date_format


def get_students_path() -> str:
    """ Get path to students file from config doc.

        :return: string with path's to file from config
        """
    config = get_config()
    config.read(SETTINGS_PATH)

    stud_path = config['Paths']['students_path']

    return stud_path


def get_rooms_path() -> str:
    """ Get path to rooms file from config doc.

        :return: string with path's to file from config
        """
    config = get_config()
    config.read(SETTINGS_PATH)

    room_path = config['Paths']['rooms_path']

    return room_path
