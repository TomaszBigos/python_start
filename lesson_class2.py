"""
Class
"""


class Animal:
    """Some Animal class 2"""
    animals = {}

    def __init__(self, species, max_speed):
        self.species = species
        self.max_speed = max_speed
        if species in Animal.animals:
            Animal.animals[species] += 1
        else:
            Animal.animals[species] = 1

    def calculate_something(self, time):
        print(time, self.max_speed)


a = Animal('Mouse', 5)
b = Animal('Horse', 25)
c = Animal('Mouse', 6)


a.calculate_something(10)
b.calculate_something(100)

print(Animal.animals)
