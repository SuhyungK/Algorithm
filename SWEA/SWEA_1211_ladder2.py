import sys
sys.stdin = open('1211.txt')

for _ in range(10):
    tc = input()
    data = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    start = []
    minV = 10000

    for s in range(102):
        if data[0][s] == 1:
            start.append(s)

    k, check = 1, 0
    for idx, j in enumerate(start):
        i = cnt = 0
        while i < 100:
            while data[i][j+k] != 0:
                j += k
                check += 1
                cnt += 1

            k *= (-1)
            check += 1
            if check > 2:
                check = 0
                i += 1
                cnt += 1

        if minV >= cnt:
            minV = cnt
            res = idx

    print('#%s %d' %(tc, start[res] - 1))
