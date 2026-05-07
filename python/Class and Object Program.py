class Car:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car Brand:", self.brand)


c1 = Car("BMW")
c1.show()
