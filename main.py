# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Main Py
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# David Levinson, 9/14/2024
# ------------------------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        import data_classes as data
        import processing_classes as proc
        import presentation_classes as present
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                       employee_data=data.employees,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    present.IO.output_menu(menu=data.MENU)

    menu_choice = present.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            present.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = present.IO.input_employee_data(employee_data=employees, employee_type=data.Employee)  # Note this is the class name (ignore the warning)
            present.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
