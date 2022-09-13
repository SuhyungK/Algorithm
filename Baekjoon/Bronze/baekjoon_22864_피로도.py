a, b, c, m = map(int, input().split())

w = cnt = 0
for h in range(24):
    if w+a <= m:
        cnt += 1
        w += a
    else:
        w -= c
        if w < 0:
            w = 0
print(cnt*b)