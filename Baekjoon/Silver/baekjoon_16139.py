# 인간-컴퓨터 상호작용

from collections import defaultdict

S = input()
q = int(input())
res = [0] * q
alp = defaultdict(int)

for tc in range(q):
    a, l, r = map(lambda x: int(x) if x.isdigit() else x, input().split())
    c = 0
    for s in S[l : r + 1]:
        if s == a:
            c += 1
    res[tc] = c

print('\n'.join(map(str, res)))