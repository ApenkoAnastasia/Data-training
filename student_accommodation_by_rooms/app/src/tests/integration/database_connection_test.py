import unittest
from app.src.students_accommodation.db_services.connectors.mysql_connector import connect_to_mysql


class TestDatabaseConnection(unittest.TestCase):
    def test_mysql_connection(self):
        config = {
            "user": "testUSER",
            "password": "testPWD",
            "host": "db_test",
            "port": 3306,
            "database": "testDB"
        }

        db_connection = connect_to_mysql(config)
        self.assertIsNotNone(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("SELECT 1")
        self.assertEqual(cursor.fetchone()[0], 1)

        db_connection.close()


if __name__ == '__main__':
    unittest.main()
