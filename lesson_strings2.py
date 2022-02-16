"""
Strings 2
"""

hello1 = "Age:" + str(9) * 2
hello2 = hello1.replace("g", "G")
hello2 = hello2.lower()
print(hello2)

hello3 = hello2.upper()
print('New format')
hello4 = "{0} {1}".format(hello3, hello2)
print(hello4)

print('Old format')
hello5 = "This number %d is %s" % (18, "age")
print(hello5)


