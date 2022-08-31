import sys
sys.stdin = open('1211.txt')

for _ in range(10):
    tc = input()
    data = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for s in range(102):
        if data[99][s] == 2:
            break

    i, j = 99, s # 시작지점
    k = 1
    check = 0
    while i > 0:
        while data[i][j+k] != 0:
            j += k
            check += 1

        k *= (-1)
        check += 1
        if check >= 2:
            i -= 1
            check = 0

    print('#%s %d' %(tc, j-1))
