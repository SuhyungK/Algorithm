m, n = map(int, input().split())
lst = []

def pn(k): # prime number
    for j in range(2, int(k ** 0.5) + 1):
        if k % j == 0:
            return
    return k

for i in range(m, n+1):
    if pn(i): lst.append(i)

print('\n'.join(map(str, lst)))
