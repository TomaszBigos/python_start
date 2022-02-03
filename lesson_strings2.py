"""
Strings 2
"""

hello1 = "Age:" + str(9) * 2
hello2 = hello1.replace("g", "G")
hello2 = hello2.lower()
print(hello2)

hello3 = hello2.upper()
hello4 = "{0} {1}".format(hello3, hello2)
print(hello4)
