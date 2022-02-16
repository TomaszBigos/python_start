fin = open('some_words.txt', 'r', encoding='utf-8')
print(fin)

fout = open('output.txt', 'w', encoding='utf-8')

count = 0
lines = ['Dobro jutro', 'Добро утро', 'Dobré ráno', 'Buenos días', 'Guten Morgen', 'Доброе утро']
for line in fin:
    count = count + 1
    lines.append(line.strip())

last_line = lines[len(lines) - 1]

print("Last line in file was:%s" %last_line)

print(fout)

lines.extend(['Buna dimineata'])

lines.sort()


for line in lines:
    fout.write(line)
    fout.write('\n')

fin.close()
fout.close()
