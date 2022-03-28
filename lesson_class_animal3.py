"""
Class , just for fun , without units and sense
"""
import sys


class Animal:
    """Animal"""

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return self.__doc__ + str(self.max_speed)

    def move(self, x):
        return (self.max_speed / 2) * x


class SomeRealAnimal(Animal):
    """Some Real animal"""

    def __init__(self, name, max_speed):
        super().__init__(max_speed)
        self.name = name

    def __str__(self):
        return 'name:' + self.name + ", max speed:" + str(self.max_speed)


class SolarAnimal(Animal):
    """Some fake animal"""

    def __init__(self):
        super().__init__(sys.maxsize)
        self.name = SolarAnimal.__doc__

    def __str__(self):
        return 'name:' + self.name + ", max speed:" + str(self.max_speed)

    def move(self, x):
        return self.max_speed * x


a = SolarAnimal()

b = SomeRealAnimal('Dog', 5)

print(a)

print(b)

print(a.move(5))

print(b.move(8))
