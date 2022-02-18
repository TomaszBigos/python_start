"""
iter
"""

list = [2, 3, 5, 17, 101, 1023]

iterator = iter(list)
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))
print(next(iterator))