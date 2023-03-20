# 핑거 스냅

def find_prime(n):
    if lst[n] == 'p': 
        return 0

    q = [n]
    while q:
        t = q.pop(0)
        for d in (t//3, t//2, t+1, t-1):
            if not (0 < d < 1000000):
                continue
            if lst[d] == 'p':
                return lst[t] + 1
            if not lst[d]:
                lst[d] = lst[t] + 1
                q.append(d)

for _ in range(int(input())):
    N, A, B = map(int, input().split())
    lst = ['p'] * (B+1) + [0] * (1000000-B)

    for i in range(2, B+1):
        if lst[i]:
            for j in range(2*i, B+1, i):
                lst[j] = 0

    if 'p' in set(l:=lst[A:]):
        lst = [0] * A + l
        print(find_prime(N))
    else:
        print(-1)