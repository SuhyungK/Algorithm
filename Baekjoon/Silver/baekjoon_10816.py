# 숫자카드 2

from collections import Counter

N = int(input())
card = Counter(list(map(int, input().split())))
M = int(input())
lst = list(map(int, input().split()))

for i in range(M):
    if card.get(lst[i]):
        lst[i] = card[lst[i]]
    else:
        lst[i] = 0

print(*lst)