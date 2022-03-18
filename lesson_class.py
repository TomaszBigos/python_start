"""
Class
"""


class Animal:
    """Some Animal class"""
    weight = 1

    def __init__(self, species, age):
        self.species = species
        self.age = age


a = Animal('Mouse', 1)

b = Animal('Horse', 5)
b.height = 1.35

print(a.__dict__)
print(b.__dict__)

print(Animal.__doc__)
