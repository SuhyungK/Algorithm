T = int(input())
for _ in range(T):
    li = []
    N = int(input())

    def binary(arr, n):
        m = n%2
        arr.append(m)
        if n == 0 or n == 1:
            return arr
        elif m:
            return binary(arr, n // 2)
        else:
            return binary(arr, n // 2)

    li = binary(li, N)

    for i, l in enumerate(li):
        if l:
            print(i, end=' ')

# 아래 풀이 안 보고 다시 풀기








t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    arr = []
    while n:
        if n % 2:
            arr.append(cnt)
        n //= 2
        cnt += 1
    print(*arr)

