import configparser


def get_config():
    config = configparser.ConfigParser()

    return config


def add_pathconfig(stud_path_cli: str, room_path_cli: str):
    config = get_config()

    config.add_section('CLI variables')
    config['CLI variables']['students_path'] = stud_path_cli
    config['CLI variables']['rooms_path'] = room_path_cli

    with open('settings.ini', 'a') as config_file:
        config.write(config_file)

    config.read('settings.ini')
    print('Params from config: ')
    print(config['CLI variables']['rooms_path'])
    print(config['CLI variables']['students_path'])
    print(config['Paths']['source_dir'])


def get_dbconfig():
    config = get_config()

    config.read('settings.ini')

    un = config['Database']['user_name']
    pas = config['Database']['password']
    host = config['Database']['host']
    db = config['Database']['db_name']
    print('Database params from config: ')
    print(un, pas, host, db)
