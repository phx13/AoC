with open("Day13.txt") as f:
    lines = f.read().split('\n')
print(lines)

# timestart = lines[0]
# bus = lines[1].replace('x,', '').split(',')
# print(bus)
#
# res = []
# for b in bus:
#     res.append(int(b) - int(lines[0]) % int(b))
# print(res)

timestart = lines[0]
bus = lines[1].split(',')
print(bus)

t = 100000000000000
while True:
    temp = t
    i = 0
    while i < len(bus):
        if bus[i] == 'x':
            i += 1
            temp += 1
        elif temp % int(bus[i]) == 0:
            i += 1
            temp += 1
        else:
            t += 1
            break
    if temp == t + len(bus):
        print(t)
        break
