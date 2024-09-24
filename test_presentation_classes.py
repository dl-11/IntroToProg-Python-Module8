# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# David Levinson,9/23/2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
import presentation_classes
import data_classes as data
from data_classes import Employee


class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = presentation_classes.IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate valid user input for employee data
        with patch('builtins.input', side_effect=['John', 'Doe', '2024-09-23', '3']):
            presentation_classes.IO.input_employee_data(self.employee_data,Employee)
            self.assertEqual(len(self.employee_data), 1)

            # Verify the values of the employee object
            employee = self.employee_data[0]
            self.assertEqual(employee.first_name, 'John')
            self.assertEqual(employee.last_name, 'Doe')
            self.assertEqual(employee.review_date, '2024-09-23')
            self.assertEqual(employee.review_rating, 3)

        # Simulate invalid review rating input (ValueError should trigger error handling, not raise)
        with patch('builtins.input', side_effect=['Alice', 'Smith', '2024-09-23', 'invalid']):
            # Call the function and check that the employee data list remains unchanged
            presentation_classes.IO.input_employee_data(self.employee_data, data.Employee)

            # Ensure that no new employee data was added due to invalid input
            self.assertEqual(len(self.employee_data), 1)  # Still only 1 employee from the previous test


if __name__ == "__main__":
    unittest.main()
