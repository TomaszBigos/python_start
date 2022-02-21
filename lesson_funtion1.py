"""
Function
List [5, 10 ,15]
0
Tuple (5, 10 ,15)
25
None
None
None
List (4, 8, 12)
"""


def multiply(elements_, multiply_):
    def multiply_as_list(elements1_, multiply1_):
        return [item * multiply1_ for item in elements1_]

    if multiply_ != 0:
        if type(elements_) == list:
            return multiply_as_list(elements_, multiply_)
        elif type(elements_) == tuple:
            return tuple(multiply_as_list(elements_, multiply_))
        elif multiply_ is None or elements_ is None:
            return None
        else:
            return elements_ * multiply_
    else:
        return 0


list5_10_15 = multiply([1, 2, 3], 5)
print(list5_10_15)

zero = multiply([7, 14, 21], 0)
print(zero)

tuple5_10_15 = multiply((1, 2, 3), 5)
print(tuple5_10_15)

simple_number = multiply(5, 5)
print(simple_number)

print(multiply(None, 5))
print(multiply(5, None))
print(multiply(None, None))

print(multiply(multiply((1, 2, 3), 2), 2))

