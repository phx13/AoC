import fileinput
import re
from copy import deepcopy
from collections import defaultdict
import math

with open('Day20.txt') as f:
    content = f.read().split('\n')

L = list([l.strip() for l in content])

G = {}
name = None
piece = []
R = 10
C = 10
for l in L:
    if 'Tile' in l:
        name = int(l.split()[1][:-1])
    elif l:
        piece.append(list(l))
    else:
        G[name] = piece
        piece = []
print(G)

EDGE = {}
for k, T in G.items():
    left = []
    right = []
    top = []
    bottom = []
    for r in range(R):
        left.append(T[r][0])
        right.append(T[r][R - 1])
    # for c in range(C):
    #     top.append(T[0][c])
    #     bottom.append(T[R - 1][c])
    top = T[0]
    bottom = T[-1]
    edges = [tuple(x) for x in [left, right, top, bottom]]
    EDGE[k] = set([x for x in edges] + [tuple(reversed(x)) for x in edges])
print(EDGE)

E = defaultdict(set)
print(E)
# Assumes if two pieces have identical boundaries they will actually be adjacent in the final puzzle
start = None
ans = 1
for k1, ET in EDGE.items():
    nbrs = 0
    for k2, EU in EDGE.items():
        if k1 != k2:
            if ET & EU:
                E[k1].add(k2)
    if len(E[k1]) == 2:
        start = k1
        ans *= k1
print(ans)
