def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("Varman", "A101", 3.9),
    Student("Narasimha", "B102", 3.7),
    Student("TIGER Muthuvel Pandian", "C103", 4.0),
    Student("Mathew", "D104", 3.5),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")