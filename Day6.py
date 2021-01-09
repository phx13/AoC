import re

r = re.compile(r'^[a-f][0-9]')
with open('Day6.txt') as file:  # Read stream
    content = file.read()
lines = content.split('\n\n')  # split content to lines
print(lines)

counter = 0
for line in lines:
    line = line.split('\n')
    temp = set('')
    for i in line:
        temp = temp.union(i)
    l = sorted(temp)
    counter += len(l)

print(counter)

counter = 0
for line in lines:
    line = line.split('\n')
    temp = set(line[0])
    for i in line:
        temp = temp.intersection(i)
    l = sorted(temp)
    counter += len(l)

print(counter)
