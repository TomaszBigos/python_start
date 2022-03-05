"""
iter
"""

list_ = [2, 3, 5, 17, 101, 1023]

iterator = iter(list_)
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))
print(next(iterator))