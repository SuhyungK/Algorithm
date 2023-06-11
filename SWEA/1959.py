# 두 개의 숫자열

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if n > m:
        L = list(map(int, input().split()))
        l = list(map(int, input().split()))
    else:
        l = list(map(int, input().split()))
        L = list(map(int, input().split()))

    res = 0
    for i in range(len(L)-len(l)+1):
        ans = 0
        for j in range(len(l)):
            ans += (L[i+j] * l[j])
        if res < ans:
            res = ans

    print(f'#{tc}', res)