#Write a function called student_marks that records marks achieved by students in a test. 
#The function should ask the user to input the name of the student and then ask the user to input the marks achieved by the student. 
#The information should be stored in a dictionary. 
#The name is the key and the marks are the value. 
# When the user enters done, the function should return a dictionary of names and values entered.

def student_marks():
    student_marks = {}
    while True:
        student = input("Enter the name of the student: ")
        if student == 'done':
            return student_marks
        marks = int(input("Enter the marks achieved by the student: "))
        student_marks[student] = marks

student_marks = student_marks()
print(student_marks)