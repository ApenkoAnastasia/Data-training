import unittest
from unittest.mock import patch
from students_accommodation.src.students_accommodation.main import main, test_connection_from_container


class TestMainFunction(unittest.TestCase):
    def test_test_connection_from_container(self):
        # Arrange
        expected_result = ...

        # Act
        result = test_connection_from_container(...)

        # Assert
        self.assertEqual(result, expected_result)

    def test_main(self):
        # Arrange
        expected_result = ...

        # Act
        result = main()

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
