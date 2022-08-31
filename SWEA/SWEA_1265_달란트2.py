T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())

    a, b = N // P, N % P
    ans = a ** (P - b) * (a + 1) ** b
    print('#%d %d'%(tc, ans))