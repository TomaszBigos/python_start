eng_2_others = dict()

words = [
'Bonjour',
'Buenos días',
'Buna dimineata',
'Cześć',
'Dobro jutro',
'Dobré ráno',
'Guten Morgen',
'Добро утро',
'Доброе утро']


eng_2_others['Hello World'] = words
eng_2_others['None'] = 'None'

print("Dictionary:")
print(eng_2_others)

print("Tuple:")
t = (words,)
print(t)

words.append("None")
print("List:")
print(words)
