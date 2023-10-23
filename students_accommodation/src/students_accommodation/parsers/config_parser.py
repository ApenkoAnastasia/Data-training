import configparser

SETTINGS_PATH = './properties/settings.ini'
DB_CONFIGS = ['user', 'password', 'host', 'port', 'database']


def get_config():
    config = configparser.ConfigParser()

    return config


def add_path_config(stud_path_cli: str, room_path_cli: str) -> None:
    config = get_config()

    config.add_section('CLI variables')
    config.set('CLI variables', 'students_path', stud_path_cli)  # insert block try-except + logging for duplicates !!!!
    config.set('CLI variables', 'rooms_path', room_path_cli)

    with open(SETTINGS_PATH, 'a') as config_file:
        config.write(config_file)


def get_db_config(db_name: str) -> dict:
    config = get_config()

    config.read(SETTINGS_PATH)

    db_config = {}

    for section in DB_CONFIGS:
        db_config[section] = config[db_name][section]

    db_config['allow_local_infile'] = True

    return db_config


def get_table_names() -> tuple[str, str]:
    config = get_config()

    config.read(SETTINGS_PATH)

    return config['Tables']['table1'], config['Tables']['table2']


def get_format_config() -> tuple[str, str]:
    config = get_config()

    config.read(SETTINGS_PATH)

    delimiter = config['Formats']['delimiter']
    date_format = config['Formats']['date_format']

    return delimiter, date_format
