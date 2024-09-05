# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using classes and functions
# Change Log: (Who, When, What)
#   RRoot,9/4/2024,Created Script
#   <Kseniia Temnikova>,<09/04/2024>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user

class FileProcessor: #Class works with file

    @staticmethod
    def read_file(file_name): #function read information from file
        try:
            file = open(file_name, "r")
            for row in file.readlines():
                # Transform the data from the file
                student_data = row.strip().split(',')
                student_dictionary = {'First name': student_data[0], 'Last name': student_data[1], 'Course': student_data[2]}
                # Load it into our collection (list of lists)
                students.append(student_dictionary)
            file.close()
        except Exception as e:
            IO.output_error_messages(
            message="There is an error while reading document, please fix that", error=e)

    @staticmethod
    def save_file(file_name): #function saves information in file
        try:
            file = open(file_name, "w")
            csv_data = ''
            for student in students:
                csv_data += f"{student['First name']},{student['Last name']},{student['Course']}\n"
            file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['First name']} {student['Last name']} is enrolled in {student['Course']}")
        except Exception as e:
            IO.output_error_messages(message="There is an is an error when the dictionary rows are written to the file, please fix that", error=e)


class IO: #class works with inputs/outputs

    @staticmethod
    def output_error_messages (message: str, error: Exception = None): #function prints caught error messages
        print(message)
        print(error, error.__doc__)

    @staticmethod
    def output_menu(menu: str): #function prints menu and returns user's choice
        print(menu)
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list): #function prints student's information
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f"Student {student['First name']} {student['Last name']} is enrolled in {student['Course']}")
        print("-" * 50)

    @staticmethod
    def input_student_data(): #function collects user's choice
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Name may consist of only alphabetic characters.")
        except Exception as e:
            IO.output_error_messages(message="There is an error during entering of first name, please fix that", error=e)
            return
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Name may consist of only alphabetic characters.")
        except Exception as e:
            IO.output_error_messages(message="There is an error during entering of last name, please fix that", error=e)
            return
        course_name = input("Please enter the name of the course: ")
        student_data = {'First name':student_first_name, 'Last name':student_last_name, 'Course':course_name}
        students.append(student_data)
        for student in students:
            print(f"You have registered {student['First name']} {student['Last name']} for {student['Course']}.")



# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

FileProcessor.read_file(FILE_NAME)

# Present and Process the data
while (True):
     # Present the menu of choices
    menu_choice = IO.output_menu(MENU)

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data()
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.save_file(FILE_NAME)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
