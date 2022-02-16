"""
Some description
Long version
"""

# comment
text = "Alice has cat"
print(text)

a, b, c = 4, 18, 16
print(a + b * c)

a = (1, 2, 3)
(x, y, z) = a
print(x + y + z)

print('Numbers as decimal')
num = (1 + 4j) + (7 - 2j) * (3 - 2j)
print('(1 + 4j) + (7 - 2j) * (3 - 2j) = {}'.format(num))

num2 = 0o15 + 0o16 - 0o13/0o01
print('0o15 + 0o16 - 0o13/0o01 = {}'.format(num2))

num3 = 0x16 + 0x1B
print('0x16 + 0x1B = {}'.format(num3))

num4 = 0b10101011 or 0b101010
print('0b10101011 or 0b101010 = {}'.format(num4))
