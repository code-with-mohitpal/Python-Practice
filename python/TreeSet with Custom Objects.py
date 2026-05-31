class Employee:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name

employees = [
    Employee(103, "Mohit"),
    Employee(101, "Rahul"),
    Employee(102, "Aman")
]

employees.sort(key=lambda x: x.empid)

for e in employees:
    print(e.empid, e.name)
