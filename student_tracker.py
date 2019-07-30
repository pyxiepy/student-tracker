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

    return student 

student = get_student()
print(student)
