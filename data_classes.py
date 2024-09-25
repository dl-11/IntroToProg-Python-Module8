# ------------------------------------------------------------------------------- #
# Title: Application Classes Module
# Description: A collection of data classes for managing the application
# ChangeLog: (Who, When, What)
# David Levinson,9/20/2024,Created Data Classes Module
# ------------------------------------------------------------------------------- #

# Data -------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        from datetime import date  # This will only import if the exception is not thrown.
except Exception as e:
    print(e.__str__())

FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - David Levinson, 9/20/2024: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a new instance of the Person class.

        :param first_name: The person's first name.
        :param last_name: The person's last name.
        """
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Returns a string representation of the Person object.

        :return: A string in the format 'first_name last_name'.
        """
        return f"{self.first_name} {self.last_name}"