def f(k):
    if k == 1:
        return False

    for i in range(2, int(k ** 0.5)):
        if k % i == 0:
            return False

    return True


m, n = map(int, input().split())

for j in range(m, n):
    if f(j):
        print(j)

