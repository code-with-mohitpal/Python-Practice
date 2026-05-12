# =========================
# Q7 Constructor Overloading
# =========================

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


p1 = Person("Mohit")
p2 = Person("Rahul", 20)
p3 = Person("Aman", 21, "Delhi")

p1.display()
p2.display()
p3.display()
