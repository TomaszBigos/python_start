"""
Lists and tuples
"""

list_ = [1, 2, 'three', 3.14]

tuple_ = (1, 2, "three", 3.14)

print(list_)
print(list_[0])
print(tuple_)
print(tuple_[0])

print(list_[1:4])
print(tuple_[1:4])

print(list_[:-2])
print(tuple_[:-2])

print(1 in list_)
print(1 in tuple_)


list_[0] = 0
print(list_)
list_[1:4] = ["one", "two", 3]
print(list_)