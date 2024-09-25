# ------------------------------------------------------------------------------- #
# Title: Presentation Classes Module
# Description: A collection of presentation classes for managing the application
# ChangeLog: (Who, When, What)
# David Levinson,9/20/2024,Created Presentation Classes Module
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import data_classes as data  # This will only import if the exception is not thrown.
except Exception as e:
    print(e.__str__())

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    David Levinson,9/20/2024,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error message to the user

        ChangeLog: (Who, When, What)
        David Levinson,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display (optional)
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        David Levinson,1.3.2030,Created function

        :param menu: string with the menu to display
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """ This function captures the user's menu choice

        ChangeLog: (Who, When, What)
        David Levinson,1.3.2030,Created function

        :return: string with the user's menu choice
        """
        return input("Please choose an option from the menu: ")

    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays the current employee data

        ChangeLog: (Who, When, What)
        David Levinson,1.3.2030,Created function

        :param employee_data: list of employee data to display
        :return: None
        """
        print("Current Employee Data:")
        for employee in employee_data:
            print(f"{employee.first_name} {employee.last_name}, {employee.employee_id}")

    @staticmethod
    def input_employee_data(employee_data: list, employee_type):
        """ This function captures new employee data from the user

        ChangeLog: (Who, When, What)
        David Levinson,1.3.2030,Created function

        :param employee_data: list to append new employee data
        :param employee_type: class type for creating new employee instances
        :return: updated list of employee data
        """
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        employee_id = input("Enter the employee ID: ")
        new_employee = employee_type(first_name, last_name, employee_id)
        employee_data.append(new_employee)
        return employee_data