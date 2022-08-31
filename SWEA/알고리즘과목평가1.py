T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2 = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]

    sumV = 0
    arr = []
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            temp = data[i][j]
            arr.append(temp)
            sumV += temp

    avgV = sumV//((r2 - r1 + 1) * (c2 - c1 + 1))
    cnt = 0
    for a in arr:
        cnt += abs(a-avgV)

    print('#%d %d'%(tc, cnt))