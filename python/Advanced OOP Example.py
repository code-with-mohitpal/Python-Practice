# Advanced OOP in Python

class Employee:
    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # Private variable

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.__salary}")

    def set_salary(self, amount):
        self.__salary = amount


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_language(self):
        print(f"{self.name} works on {self.language}")


d1 = Developer("Mohit", 80000, "Python")

d1.show_details()
d1.show_language()
