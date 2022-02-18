"""
if
"""

if True:
    print('True')

if 'String':
    print('String')

if -1:
    print('-1')

if 0:
    print(0)

if None:
    print(Nan)

x = int(input('Put the number:'))
if x > 0:
    print('{} > 0'.format(x))
elif x == 0:
    print('{} == 0'.format(x))
else:
    print('{} < 0'.format(x))
