n = int(input())
cnt = 0

for i in range(3, 6, 2):
    if not n % i:
        cnt = n // i
        print(cnt)
        break
else:
    while n > 0:
        n -= 5
        cnt += 1

    if n != 0:
        n += 5
        cnt -= 1
        while n > 0:
            n -= 3
            cnt += 1

    if n == 0:
        print(cnt)
    else:
        print(-1)