# 1. Create record for new student
# 2. Modify student information
# 3. Search for student
# 4. Search students with course
# 5. List of students
# 6. Quit (Data will be stored into a file (JSON))

import json
from datetime import datetime

# Declare variables, student_list (dictionary) as database
student_list = []
id = None
name  = None
date_of_birth = None
course = None


# Get student id and perform validation
def get_student_id():

    valid_id = False

    # When student_id is not valid, keep running this block until it is valid and returns valid student_id
    # If user inserts 'quit', return exit as True (Bool)
    while valid_id == False:
        student_id = input("Enter ID ('quit' to exit): ").lower()

        # If student_id equals 'quit', return exit as True (Bool)
        if student_id == 'quit':
            exit = True
            return exit

        # If student_id is not blank, length exceed 2 characters, and first two characters are 'tp'
        elif student_id is not None and len(student_id) > 2 and student_id[:2] == 'tp':

            # return lowercase student_id
            return student_id.lower()
            valid_id = True

        # Else, it is invalid
        else:
            print('\nInvalid ID (Exp: tp123)\n')
            valid_id = False


# Get student name and perform validation
def get_student_name():

    valid_name = False

    # When student_name is not valid, keep running this block until it is valid
    while valid_name == False:

        student_name = input('Enter Name: ')

        # If student_name is not blank, length exceed 2 characters, and it is all alphabet with spacing is enabled
        if student_name is not None and len(student_name) > 2 and student_name.replace(' ', '').isalpha():

            # return lowercase student_name
            return student_name.lower()
            valid_name = True

        else:
            print('\nInvalid name\n')
            valid_name = False


# Get student date of birth and perform validation
def get_student_date_of_birth():

    valid_date_of_birth = False

    # When student_date_of_birth is not valid, keep running this block until it is valid
    while valid_date_of_birth == False:
        student_date_of_birth = input('Enter Date of Birth (dd/mm/yyyy): ')

        # Try to fit user input into Date format
        try:
            # Date format: dd/mm/yyyy
            birthday = datetime.strptime(student_date_of_birth, '%d/%m/%Y')

            # Find days between date today and date of birth
            difference = datetime.today().date() - birthday.date()

            # 3650 days = 10 years, 10950 days = 30 years, if user is between 10 and 30 years old, return the date of birth
            if difference.days >= 3650 and difference.days <= 10950:
                return student_date_of_birth
                valid_date_of_birth = True

            elif difference.days < 0:
                print('\nInvalid date\n')

            elif difference.days > 10950:
                print('\nThe student is above age of 30 years old. Please try again.\n')

            else:
                print('\nThe student is under age of 10 years old. Please try again.\n')

        # If user input couldn't fit into Date format
        except ValueError:
            print('\nInvalid date\n')
            valid_date_of_birth = False


# Get student course
def get_student_course():
    student_course = input('Enter Course: ')
    return student_course.lower()


# Create new record for new student
def add_student():

    exit = False

    # When user not inserting 'quit', keep running this block
    while exit == False:

        # Get id by FUNCTION, it returns TRUE (Bool) to exit this function or it returns student_id for creating new student record
        id = get_student_id()

        # If it returns TRUE (Bool), exit this function
        if id == True:

            exit = True

        # If there is no same student_id in student_list
        elif not any(dict['ID'] == id for dict in student_list):

            student_name = get_student_name()
            student_date_of_birth = get_student_date_of_birth()
            student_course = get_student_course()

            # Get date today in format dd/mm/yyyy
            date_today = datetime.today().strftime('%d/%m/%Y')

            student_list.append({
                'ID': id,
                'Day Registered': date_today,
                'Name': student_name,
                'DOB' : student_date_of_birth,
                'Course': student_course
            })
            print('\nInformation of ' + student_name + ' is stored successfully!\n')

        else:
            print('\nID existed, please try again!\n')


# Modify student information
def modify_student():

    exit = False

    # When user not inserting 'quit', keep running this block
    while exit == False:

        found = False

        # Get id by FUNCTION, it returns TRUE (Bool) to exit this function or it returns student_id for modifying student record
        id = get_student_id()

        if id == True:

            exit = True

        else:
            for dict in student_list:

                if dict['ID'] == id:

                    print('-----------------------------------')
                    print('ID: ' + dict['ID'])
                    print('Day Registered: ' + dict['Day Registered'])
                    print('Student Name: ' + dict['Name'])
                    print('Student Date of Birth: ' + dict['DOB'])
                    print('Student Course: ' + dict['Course'])
                    print('-----------------------------------')

                    found = True

                    modify = input('Modify? (yes / no): ').lower()
                    print('\n')

                    if modify == 'yes':
                        new_student_name = get_student_name()
                        new_student_date_of_birth = get_student_date_of_birth()
                        new_course = get_student_course()

                        dict['Name'] = new_student_name
                        dict['DOB'] = new_student_date_of_birth
                        dict['Course'] = new_course

                        print('\nInformation of ' + new_student_name + ' is updated successfully!\n')

                    elif modify == 'no':
                        pass

                    else:
                        print('\nInvalid answer, please try again.\n')

            if found == False:
                print('\nStudent doesn\'t exist \n')


# Search for specific student with ID
def search_student():

    exit = False

    while exit == False:

        found = False
        id = get_student_id()

        if id == True:

            exit = True

        else:
            for dict in student_list:

                if dict['ID'] == id:
                    print('-----------------------------------')
                    print('ID: ' + dict['ID'])
                    print('Day Registered: ' + dict['Day Registered'])
                    print('Student Name: ' + dict['Name'])
                    print('Student Date of Birth: ' + dict['DOB'])
                    print('Student Course: ' + dict['Course'])
                    print('-----------------------------------')

                    found = True

        if found == False:
            print('\nStudent doesn\'t exist \n')


# Search students in specific course
def search_course_student():

    exit = False

    while exit == False:

        found = False

        course = input("\nEnter Course ('quit' to exit): ").lower()

        if course == 'quit':
            exit = True

        else:
            for dict in student_list:

                if dict['Course'] == course:

                    print(dict)
                    found = True

        if found == False:
            print('\nCourse doesn\'t exist')


# Show entire student list
def show_student_list():

    if len(student_list) > 0:
        for dict in student_list:
            print(dict)
    else:
        print('There is no student record in the database.')


# Try to open and read the student.json
try:
    with open("student.json", "r") as file:

        # Try to load the data from the student.json into student_list
        try:
            student_list = json.load(file)

        # In case the file is not in .json format
        except json.decoder.JSONDecodeError:
            print('Database is not in .json file format')

# If student.json is not found, ignore first, the file will be created at the end
except FileNotFoundError:
    print('Database is not found, a new database will be created later')


# Launch application
while True:
    print('\n')
    print('==========Welcome to Student Management System==========')
    print('Options:')
    print('1. Add new student')
    print('2. Modify student information')
    print('3. Search for student')
    print('4. Search students with course')
    print('5. List of students')
    print('0. Quit\n')

    choice = input('Choice: ')
    print('-----------------------------------\n')

    # Add new student
    if choice == '1':
        print('Add new student')
        print('-----------------------------------')
        add_student()

    # Modify student information
    elif choice == '2':
        print('Modify student information')
        print('-----------------------------------')
        modify_student()

    # Search for student
    elif choice == '3':
        print('Search for student')
        print('-----------------------------------')
        search_student()

    # Search students with course
    elif choice == '4':
        print('Search students with course')
        print('-----------------------------------')
        search_course_student()

    # List of student
    elif choice == '5':
        print('List of students')
        print('-----------------------------------')
        show_student_list()

    # Quit application
    elif choice == '0':

        # Store student_list into student.json, if the file not exist create one (w+)
        json.dump(student_list, open('student.json', 'w+'))
        print('Storing data...')
        print('Shutting down...')
        break

    else:
        print('Invalid number\n')
