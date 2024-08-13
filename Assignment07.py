# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   NPlaza,8/10/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

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
FILE_NAME: str = "Enrollments.json"

# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor
# TODO Create a getter and setter for the first_name property
# TODO Create a getter and setter for the last_name property
# TODO Override the __str__() method to return Person data

# TODO Create a Student class the inherits from the Person class
# TODO call to the Person constructor and pass it the first_name and last_name data
# TODO add a assignment to the course_name property using the course_name parameter
# TODO add the getter for course_name
# TODO add the setter for course_name
# TODO Override the __str__() method to return the Student data

# Person and Student Classes --------------------------------------- #


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        """
        Returns the first name in title case
        :return: first name w proper capital case

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        """
        return self._first_name.title()

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Sets first Name w Non-Numeric Validation
        :param value: set value

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        """
        if value.isalpha():
            self._first_name = value
        else:
            raise ValueError("First name must not contain numbers")

    @property
    def last_name(self) -> str:
        """
        Returns the last name in title case
        :return: last name w proper capital case

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        """
        return self._last_name.title()

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets last name w Non-Numeric Validation
        :param value: set value

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        """
        if value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name must not contain numbers")

    def __str__(self) -> str:
        """
        Str Function for Person
        :return: string as CSV

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created
        :return: None
        """
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name: str, last_name: str, course_name: str):
        super().__init__(first_name, last_name)
        self.course_name = course_name

    @property
    def course_name(self) -> str:
        '''
        Returns Course Name
        :return: course_name
        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created
        '''
        return self._course_name

    @course_name.setter
    def course_name(self, value: str) -> None:
        self._course_name = value

    def __str__(self) -> str:
        '''
        Str Function for Person
        ::return: string as CSV
        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created
        '''
        return f"{self.first_name} {self.last_name}, {self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    NPlaza August 11, 2024,Edited Class to call from list[student]
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[Student]) -> list[Student]:
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                file_data = json.load(file)
            for row in file_data:
                student_data.append(Student(row["first_name"], row["last_name"], row["course_name"]))
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[Student]) -> None:
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file_data = []
        for student in student_data:
            file_data.append({
                "first_name": student.first_name,
                "last_name": student.last_name,
                "course_name": student.course_name
            })
        try:
            with open(file_name, "w") as file:
                json.dump(file_data, file, indent=4)
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    NPlaza, August 11, 2024, Created
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created
        :param message: string with message data to display
        :param error: Exception object with technical message to display
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created
        :return: None
        """
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]) -> None:
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list[Student]) -> list[Student]:
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        NPlaza, August 11, 2024, Created

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student = Student(student_first_name, student_last_name, course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Main Body of Script ------------------------------------------------------- #
students: list[Student] = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Input user data
        students = IO.input_student_data(student_data=students)
        continue
    elif menu_choice == "2":  # Present the current data
        IO.output_student_and_course_names(student_data=students)
        continue
    elif menu_choice == "3":  # Save the data to a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    elif menu_choice == "4":  # Stop the loop
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
