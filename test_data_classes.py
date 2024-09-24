# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# David Levinson,9/23/2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest, data_classes


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = data_classes.Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):  # Testing that isalpha works as expected and raises error
            person = data_classes.Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = data_classes.Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = data_classes.Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = data_classes.Employee("Alice", "Smith", "2024-09-23", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2024-09-23")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_date_type(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            employee = data_classes.Employee("Bob", "Johnson", "invalid_dt")

    def test_employee_str(self):
        employee = data_classes.Employee("Eve", "Brown", "2024-09-23", 4)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve,Brown,2024-09-23,4")


if __name__ == '__main__':
    unittest.main()
