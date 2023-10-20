from typing import Tuple, List

import mysql.connector as mc
from mysql.connector import MySQLConnection, CMySQLConnection
from mysql.connector.constants import ClientFlag
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor
from mysql.connector.pooling import PooledMySQLConnection


def db_connect(config: dict) -> list[
    PooledMySQLConnection | MySQLConnection | CMySQLConnection | MySQLCursor | CMySQLCursor]:
    """

    :rtype: list
    """
    try:
        cnx = mc.connect(**config)
        if cnx.is_connected():
            print(f"Connected to database: {config['database']}")
            cursor = cnx.cursor()

            cursor_config = [cnx, cursor]
            return cursor_config
    except Exception as e:
        print("Doesn't connect to DB.")


def load_data(config: dict):
    """

    :param config: dict
    """

    cursor_config = db_connect(config)

    # cursor.callproc('selectResultProcedure', args)
    cnx, cursor = cursor_config

    cursor.close()

    cnx.close()
