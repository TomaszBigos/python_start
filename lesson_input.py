name = input('What is your name:')

print('Method for input')
print(dir(name))
length = len(name)
print(name[0:length])
print(name[2:length])
print(name[:length])
print(name[2:])


if 'a' in name:
    print('a was found in %d letters' % length)

if 'z' in name:
    print('z was found in {0} letters'.format(length))
