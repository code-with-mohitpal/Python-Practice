# =========================
# Q9 Multiple Inheritance
# =========================

class Herbivore:
    def eat_grass(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    pass


b = Bear()
b.eat_grass()
b.eat_meat()
b.eat_both()
