# =========================
# Q6 Abstraction
# =========================

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        return 10000


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000


i = Intern()
f = FullTimeEmployee()
c = ContractEmployee()

print("Intern Salary:", i.calculate_salary())
print("Full Time Salary:", f.calculate_salary())
print("Contract Salary:", c.calculate_salary())

