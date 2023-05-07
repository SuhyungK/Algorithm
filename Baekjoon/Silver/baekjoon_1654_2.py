K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

lo, hi = 1, max(lan)
while lo <= hi:
    m = (lo+hi) // 2
    cnt = 0
    for l in lan:
        cnt += l // m
        if cnt >= N:
            break
    print(m, cnt, lo, hi)
    if cnt >= N:
        lo = m + 1
    else:
        hi = m - 1

print(lo)