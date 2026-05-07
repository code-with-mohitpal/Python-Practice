class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.sound()
d.bark()
