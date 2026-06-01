class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [
    Employee("Mohit", 50000),
    Employee("Rahul", 30000),
    Employee("Aman", 70000)
]

employees.sort(key=lambda e: e.salary)

for e in employees:
    print(e.name, e.salary)
