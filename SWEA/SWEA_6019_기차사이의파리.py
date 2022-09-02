T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())

    ans = d / (a + b) * f
    print('#%d %f'%(tc, ans))