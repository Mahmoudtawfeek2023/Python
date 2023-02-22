max_students = 4
max_score = 4

student_score = []
student_name = []

for score in range(max_score):
    studentscore = float(input("The student score is: "))
    student_score.append(studentscore)

for student in range(max_students):
    studentname = input("The student name is: ")
    student_name.append(studentname)
    
class_name_test = [list(a) for a in zip(student_name, student_score)]
print(class_name_test)