"""
Generator
"""


def gen(a, b):
    for i in range(a):
        yield i * a << b


generator = gen(10, 2)

print(next(generator))
print(next(generator))
print(next(generator))

