# 소수구하기

import math

def decimal(num):
    if num == 1:
        return

    elif num == 2:
        lst.append(2)
        return

    elif num % 2 == 0:
        return

    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            break
    else:
        lst.append(num)

m, n = map(int, input().split())
lst = []
for num in range(m, n+1):
    decimal(num)

print('\n'.join(map(str, lst)))