# = "Aisha"
#student1_gpa = 3.8
#
# = "Diego"
#student2_gpa = 3.2
#
# print_student(name, gpa):
#    print(f"{name}: GPA {gpa}")
#
#print_student(student1_name, student1_gpa)
#print_student(student2_name, student2_gpa)
 
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
s1 = Student('Aisha', 3.8)
s2 = Student('Diego', 3.2)
print(s1.name)
print(s2.name)

avg = 0.0
total = 0.0
for s in students:
    total += s.gpa
    
    
print(f'The average is {total/len(students):.2f}')