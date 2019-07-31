import os

'''Web App to keep track of student progress.'''

students = []


def get_student():
    '''Properly format and add a student to the database
    
    Returns: student as a dictionary
    '''    
    
    name = ''
    student_id = ''

    while not name:
        name = input("Enter student name:\n")
 
    while not student_id:
        s = input("Enter student ID (a letter followed by 4 numbers):\n")

        if len(s) == 5:
            letter = s[:1]
            if not letter.isalpha():
                print(f"First character '{letter}' should be a letter.") 
                continue
 
            num_text = s[1:]
            try:
                number = int(num_text)
            except ValueError:
                print(f"Invalid ID: last 4 characters should be numbers")
            else:
                student_id = letter + str(number)

        else:
            print("Invalid entry")
    
    student = {"name": name.title(), "student_id": student_id.title()}
    students.append(student)

    return student 


def append_file(student):
    '''Add each student's name to a file.

        Args:
            student:    The student's name only
    '''

    try:
        with open('students.txt', 'a') as f:
            f.write(student['name'] + '\n')
    except FileNotFoundError as e:
        print(f'Error: {e}\nCould not open file.') 


def print_file_contents():
    '''Print the current student database.'''

    with open('students.txt', 'r') as f:
        for name in f.readlines():
            print(name)


enter_student = 'y'

while enter_student == 'y':
    student = get_student()
    append_file(student)
    enter_student = input('Enter another student? "y" for yes, and "n" for no:  ').lower()


print('Current student list:')

print_file_contents()
