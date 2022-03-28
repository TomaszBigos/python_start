"""
Class
"""


class Animal:
    """Some Animal class"""
    weight = 1

    def __init__(self, species, age, max_speed):
        self.species = species
        self.age = age
        self.max_speed = max_speed

    def calculate_distance(self, time):
        print(time, self.max_speed)


a = Animal('Mouse', 1, 5)

b = Animal('Horse', 5, 25)
b.height = 1.35

print(a.__dict__)
print(b.__dict__)

print(Animal.__doc__)

a.calculate_distance(100)
b.calculate_distance(125)



