class Student:
    def __init__(self, marks):
        self.marks = marks

students = [
    Student(80),
    Student(95),
    Student(70)
]

students.sort(key=lambda s: s.marks, reverse=True)

for s in students:
    print(s.marks)
