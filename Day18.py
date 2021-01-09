import fileinput
import re

with open('Day18.txt') as f:
    content = f.read().split('\n')
# print(content)
#
# r = re.compile('\(+.+\)')
# ress = []
# for l in content:
#     res = [l]
#     temp = re.findall(r, l)
#     while len(temp) > 0:
#         l = temp[0][1:-1]
#         temp = re.findall(r, l)
#         res.append(l)
#     ress.append(res)
# print(ress)

# Term := LIT | \( EMul \)
# EAdd := Term (+ Term)*
# EMul := EAdd (\* EAdd)*

def Term(W, i):
    if W[i]=='(':
        v,i2 = EMul(W, i+1)
        assert W[i2] == ')', W[i2]
        return (v, i2+1)
    else:
        return (int(W[i]),i+1)

def EAdd(W, i):
    t1,i2 = Term(W, i)
    ans = t1

    while True:
        if i2 == len(W) or W[i2] == ')' or W[i2]=='*':
            return ans,i2
        else:
            assert W[i2] == '+'
            t2, i3 = Term(W, i2+1)
            ans = ans+t2
            i2 = i3

def EMul(W, i):
    t1,i2 = EAdd(W, i)
    ans = t1
    while True:
        if i2 == len(W) or W[i2] == ')':
            return ans,i2
        else:
            assert W[i2] == '*'
            t2, i3 = EAdd(W, i2+1)
            ans = ans*t2
            i2 = i3

# TermP1 := LIT | \( EXPR \)
# Expr := TermP1 (OP TermP1)*

# Each line can be parsed as an Expr

# Gives you back the value of the term and the *next* word to parse
def TermP1(W, i):
    if W[i]=='(':
        v,i2 = Expr(W, i+1)
        assert W[i2] == ')', W[i2]
        return (v, i2+1)
    else:
        return (int(W[i]),i+1)

def eval1(first, op, second):
    if op == '+':
        return first+second
    else:
        assert op == '*'
        return first*second

# evaluate expression starting at W[i] until ')' or end
def Expr(W, i):
    t1,i2 = TermP1(W, i)
    ans = t1

    while True:
        if i2 == len(W) or W[i2]==')':
            return ans,i2
        else:
            assert W[i2] in ['+', '*'], W[i2]
            t2, i3 = TermP1(W, i2+1)
            ans = eval1(ans, W[i2], t2)
            i2 = i3

def solve(p1):
    ans = 0
    L = list([l.strip() for l in content])
    for l in L:
        l = l.replace('(', '( ')
        l = l.replace(')', ' )')
        words = l.split()
        v,idx = (Expr if p1 else EMul)(words, 0)
        ans += v
        assert idx == len(words)
    return ans
print(solve(True))
print(solve(False))
