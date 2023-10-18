import configparser


def get_config():
    config = configparser.ConfigParser()

    return config


def add_path_config(stud_path_cli: str, room_path_cli: str):
    config = get_config()

    config.add_section('CLI variables')
    config.set('CLI variables', 'students_path', stud_path_cli)  # insert block try-except + logging for duplicates !!!!
    config.set('CLI variables', 'rooms_path', room_path_cli)

    with open('settings.ini', 'a') as config_file:
        config.write(config_file)


def get_db_config():
    config = get_config()

    config.read('settings.ini')

    un = config['Database']['user_name']
    pas = config['Database']['password']
    host = config['Database']['host']
    db = config['Database']['db_name']
    print('Database params from config: ')
    print(un, pas, host, db)


def get_format_config() -> tuple[str, str]:
    config = get_config()

    config.read('settings.ini')

    delimiter = config['Formats']['delimiter']
    date_format = config['Formats']['date_format']

    return delimiter, date_format
