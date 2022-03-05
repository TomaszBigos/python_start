"""
Function 2
"""

list_ = [a * 5 for a in (1, 2, 3, 4, 5)]


def execute(a, *args):
    iterator_ = iter(args)
    x = a * iterator_.__next__()
    return x


print(execute(list_, 2, 3))
