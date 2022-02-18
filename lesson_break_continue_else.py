"""
break, continue, else
"""

x = 0
y = []
while True:
    x += 1
    print(x)
    y.append(x)
    if x == 3:
        break

while x < 10:
    x += 1
    if x % 2 == 0:
        y.append(x)
        continue
    print(x)

while x < 36:
    x += 1
    if x % 18 == 0:
        y.append(x)
        break

print(y)
