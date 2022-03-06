"""
Lambda
"""

l = lambda a, b, c: a + b + c

print(l(2, 3, 4))
print("--------------")

list_ = [(lambda a: a * -2), (lambda a: a * 2),  (lambda a: a * -3),  (lambda a: a * 3)] * 20
x = 0

for item in list_:
    x = item(7)

print(x)
