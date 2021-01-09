import fileinput
import re
from copy import deepcopy
from collections import defaultdict
import math

with open('Day22.txt') as f:
    content = f.read().split('\n\n')
    p1 = content[0]
    p2 = content[1]

player1 = list([l.strip() for l in p1.split('\n')])[0]
player1cards = list([l.strip() for l in p1.split('\n')])[1:]
print(player1)
print(player1cards)

player2 = list([l.strip() for l in p2.split('\n')])[0]
player2cards = list([l.strip() for l in p2.split('\n')])[1:]
print(player2)
print(player2cards)

flag = True
while flag:
    if int(player1cards[0]) > int(player2cards[0]):
        player1cards.append(player1cards[0])
        player1cards.append(player2cards[0])
        player1cards.remove(player1cards[0])
        player2cards.remove(player2cards[0])
    elif int(player1cards[0]) < int(player2cards[0]):
        player2cards.append(player2cards[0])
        player2cards.append(player1cards[0])
        player1cards.remove(player1cards[0])
        player2cards.remove(player2cards[0])

    if len(player1cards) == 0 or len(player2cards) == 0:
        flag = False

ans = 0
if len(player1cards) == 0:
    for i in range(len(player2cards)):
        ans += int(player2cards[i]) * (len(player2cards) - i)
else:
    for i in range(len(player1cards)):
        ans += int(player1cards[i]) * (len(player1cards) - i)
print(ans)


import fileinput
import re
from collections import deque
from copy import deepcopy

D1 = deque()
D2 = deque()
active_deck = D1

with open('Day22.txt') as f:
    content = f.read().split('\n')
L = list([l.strip() for l in content])
for l in L:
    if 'Player' in l:
        if '2' in l:
            active_deck = D2
    elif l:
        active_deck.append(int(l))

t = 0
def play_game(D1, D2, is_p2):
    SEEN = set()
    while D1 and D2:
        global t
        t += 1
        my_key = (tuple(D1),tuple(D2))
        if my_key in SEEN and is_p2:
            return True,D1
        SEEN.add(my_key)
        c1,c2 = D1.popleft(), D2.popleft()
        if len(D1)>=c1 and len(D2)>=c2 and is_p2:
            NEW_D1 = deque([D1[x] for x in range(c1)])
            NEW_D2 = deque([D2[x] for x in range(c2)])
            p1_wins,_ = play_game(NEW_D1, NEW_D2, is_p2)
        else:
            p1_wins = c1>c2

        if p1_wins:
            D1.append(c1)
            D1.append(c2)
        else:
            D2.append(c2)
            D2.append(c1)
    if D1:
        return True,D1
    else:
        return False,D2

for p2 in [False,True]:
    p1,winner_deck = play_game(deepcopy(D1),deepcopy(D2),p2)
    score = 0
    for i,c in enumerate(winner_deck):
        score += (len(winner_deck)-i)*c
    print(score)
