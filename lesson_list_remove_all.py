"""
Lists remove all '2'
"""

list_ = [1, 2, 'three', 3.14, 1, 2, 3, 2]
list_[2] = 2
list_[3:4] = [[1, 2, 3], [7, 8, [5, 6]]]
list_ = list_ + [1, 2, 3, 4, 2, [1, 2]]
print(list_)

# Sort is not working in that case "TypeError: '<' not supported between instances of 'list' and 'int'"
# list_.sort()

print('List reverse')
list_.reverse()

# Count only on 0 level
print(list_.count(2))
# TODO to be continue
list_.remove(2)
print(list_)
