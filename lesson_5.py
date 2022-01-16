name = input('What is your name:')

print('Method for input')
print(dir(name))
len = len(name)
print(name[0:len])
print(name[2:len])
print(name[:len])
print(name[2:])


if 'a' in name:
    print('a was found in %d letters' %len)

if 'z' in name:
    print('z was found in {0} letters'.format(len))
