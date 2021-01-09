import re

r = re.compile(r'^[a-f][0-9]')
with open('Day5.txt') as file:  # Read stream
    content = file.read()
lines = content.split('\n')  # split content to lines
print(lines)


def FB(str, start, end, i):
    if i < 6:
        if str[i] == 'F':
            s = start
            e = (start + end - 1) / 2
        else:
            s = (start + end + 1) / 2
            e = end
        return FB(str, s, e, i + 1)

    if i == 6:
        if str[i] == 'F':
            ress = start
        else:
            ress = end
        return int(ress)


def LR(str, start, end, i):
    if i < 2:
        if str[i] == 'L':
            s = start
            e = (start + end - 1) / 2
        else:
            s = (start + end + 1) / 2
            e = end
        return LR(str, s, e, i + 1)

    if i == 2:
        if str[i] == 'L':
            ress = start
        else:
            ress = end
        return int(ress)


temp = 0
l = []
for line in lines:
    res1 = FB(line[:7], 0, 127, 0)
    res2 = LR(line[7:], 0, 7, 0)
    l.append([res1, res2])
    if res1 * 8 + res2 > temp:
        temp = res1 * 8 + res2

print(temp)
print(l)

chessboard = [[0] * 8 for i in range(128)]  # Define chessboard
for i in l:
    chessboard[i[0]][i[1]] = 1

print(chessboard)
