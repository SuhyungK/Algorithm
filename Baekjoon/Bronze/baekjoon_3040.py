# 백설공주와 일곱 난쟁이

from itertools import combinations

lst = [int(input()) for _ in range(9)]
for comb in combinations(lst, 7):
    if sum(comb) == 100:
        break

print('\n'.join(map(str, list(comb))))