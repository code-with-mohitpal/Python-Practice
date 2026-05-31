class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return f"{self.id} {self.name}"

students = [
    Student(3, "Mohit"),
    Student(1, "Rahul"),
    Student(2, "Aman")
]

students.sort()

print(students)
