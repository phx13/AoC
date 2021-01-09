with open("Day12.txt") as f:
    lines = f.read().split('\n')
print(lines)

start = [0, 0]
di = 0
for line in lines:
    a = line[:1]
    s = int(line[1:])
    if a == 'F':
        if di % 360 == 0:
            a = 'E'
        elif di % 360 == 90:
            a = 'S'
        elif di % 360 == 180:
            a = 'W'
        elif di % 360 == 270:
            a = 'N'

    if a == 'E':
        start[0] += s
    elif a == 'S':
        start[1] += s
    elif a == 'W':
        start[0] -= s
    elif a == 'N':
        start[1] -= s

    if a == 'L':
        di -= s
    elif a == 'R':
        di += s
    elif a == 'F':
        di = di
res = abs(start[0]) + abs(start[1])
print(res)

start = [0, 0]
waypoint = [10, -1]
di = 0
for line in lines:
    a = line[:1]
    s = int(line[1:])
    if a == 'F':
        start[0] += s * waypoint[0]
        start[1] += s * waypoint[1]

    if a == 'E':
        waypoint[0] += s
    elif a == 'S':
        waypoint[1] += s
    elif a == 'W':
        waypoint[0] -= s
    elif a == 'N':
        waypoint[1] -= s

    if a == 'L':
        while s:
            waypoint = [waypoint[1], -waypoint[0]]
            s -= 90
    elif a == 'R':
        while s:
            waypoint = [-waypoint[1], waypoint[0]]
            s -= 90
res = abs(start[0]) + abs(start[1])
print(res)
