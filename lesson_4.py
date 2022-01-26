import random


def print_(a, b):
    print(a / b)


t = [5, 10, 15]

n = 50
while n > 0:
    x = random.randint(5, 15)
    y = random.choice(t)
    print_(x, y)
    n = n - 1
