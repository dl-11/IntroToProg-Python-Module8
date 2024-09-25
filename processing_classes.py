# ------------------------------------------------------------------------------- #
# Title: Application Classes Module
# Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# David Levinson,9/20/2024,Created Processing Classes Module
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import json
        import data_classes as data  # This will only import if the exception is not thrown.
except Exception as e:
    print(e.__str__())

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    David Levinson,9/20/2024,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: data.Employee):
        """ This function reads data from a JSON file and loads it into a list of employee objects

        ChangeLog: (Who, When, What)
        David Levinson,9/20/2024,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list to be filled with employee objects
        :param employee_type: a reference to the Employee class
        :return: list of employee objects
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            print(f"Error: {file_name} not found. {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_name}. {e}")
        except Exception as e:
            print(f"An error occurred while reading from {file_name}. {e}")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a JSON file from a list of employee objects

        ChangeLog: (Who, When, What)
        David Levinson,9/20/2024,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of employee objects to be written to the file
        :return: None
        """
        try:
            list_of_dictionary_data = []
            for employee in employee_data:
                employee_dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_dict)
            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError as e:
            print(f"Error: Data type issue. {e}")
        except Exception as e:
            print(f"An error occurred while writing to {file_name}. {e}")