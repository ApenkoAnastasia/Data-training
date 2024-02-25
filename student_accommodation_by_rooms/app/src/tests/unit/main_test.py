import unittest
from unittest.mock import patch
from app.src.students_accommodation.main import main, test_connection_from_container



class TestMainFunction(unittest.TestCase):
    def test_connection(self):
        config = {
            "user": "testUSER",
            "password": "testPWD",
            "host": "db_test",
            "port": 3306,
            "database": "testDB"
        }

        db_connection = test_connection_from_container(config)
        self.assertIsNotNone(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("SELECT 1")
        self.assertEqual(cursor.fetchone()[0], 1)

        db_connection.close()

    def test_main(self):
        # expected_result = 0 for success exit

        result = main()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
