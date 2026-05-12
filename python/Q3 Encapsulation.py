# =========================
# Q3 Encapsulation
# =========================

class Student:
    def __init__(self):
        self._name = ""
        self._roll_no = 0
        self._marks = 0

    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            print("Name cannot be empty")

    def get_name(self):
        return self._name

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Invalid Roll Number")

    def get_roll_no(self):
        return self._roll_no

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")

    def get_marks(self):
        return self._marks


s = Student()
s.set_name("Rahul")
s.set_roll_no(25)
s.set_marks(89)

print(s.get_name())
print(s.get_roll_no())
print(s.get_marks())
