class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __repr__(self):
        return f"{self.name} {self.marks}"

students = [
    Student("Mohit", 85),
    Student("Rahul", 70),
    Student("Aman", 90)
]

students.sort()

print(students)
