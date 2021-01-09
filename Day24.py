with open('Day24.txt') as f:
    content = f.read().split('\n')

print(content)

dict = []
for l in content:
    x, y, z = 0, 0, 0
    while l:
        if l.startswith('e'):
            x += 1
            y -= 1
            l = l[1:]
        elif l.startswith('se'):
            y -= 1
            z += 1
            l = l[2:]
        elif l.startswith('sw'):
            x -= 1
            z += 1
            l = l[2:]
        elif l.startswith('w'):
            x -= 1
            y += 1
            l = l[1:]
        elif l.startswith('nw'):
            z -= 1
            y += 1
            l = l[2:]
        elif l.startswith('ne'):
            x += 1
            z -= 1
            l = l[2:]
        else:
            assert False

    if (x, y, z) in dict:
        dict.remove((x, y, z))
    else:
        dict.append((x, y, z))

print(len(dict))

for _ in range(100):
    newB = set()
    CHECK = set()
    for (x,y,z) in dict:
        CHECK.add((x,y,z))
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            CHECK.add((x+dx,y+dy,z+dz))

    for (x,y,z) in CHECK:
        nbr = 0
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            if (x+dx,y+dy,z+dz) in dict:
                nbr += 1
        if (x,y,z) in dict and (nbr==1 or nbr==2):
            newB.add((x,y,z))
        if (x,y,z) not in dict and nbr==2:
            newB.add((x,y,z))
    dict = newB
print(len(dict))