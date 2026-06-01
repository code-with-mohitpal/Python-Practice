class Student:
    def __init__(self, name):
        self.name = name

students = [
    Student("Mohit"),
    Student("Aman"),
    Student("Rahul")
]

students.sort(key=lambda s: s.name)

for s in students:
    print(s.name)
