def dfs(idx, sumV, lst):
    global maxV
    if len(lst) == k:
        if maxV < sumV:
            maxV = sumV

    for i in range(idx, n):
        if len(lst) >= k:
            break
        elif i in lst:
            continue
        dfs(i+1, sumV + score[i], lst + [i])


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    maxV = 0
    dfs(0, 0, [])

    print(f'#{tc}', maxV)