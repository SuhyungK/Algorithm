# 리모컨

from itertools import product

N = int(input())
M = int(input())
BUTTONS = {i for i in range(0, 10)}
if M != 0:
    BUTTONS -= set(map(int, input().split()))

count = abs(N - 100)
target_len = len(str(N))
for l in (target_len-1, target_len, target_len+1):
    if l == 0:
        continue
    for i in product(list(BUTTONS), repeat=l):
        tmp = int(''.join(map(str, i)))
        count = min(count, abs(N-tmp) + len(str(tmp)))

print(count)