def check():
    lst = [-1] * 10
    k = 1
    for row in arr:
        for num in row:
            if lst[num] == k:
                return 0
            lst[num] = k
        k *= (-1)

    re_arr = list(map(list, zip(*arr)))

    for row in re_arr:
        for num in row:
            if lst[num] == k:
                return 0
            lst[num] = k
        k *= (-1)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for n in range(3):
                for m in range(3):
                    if lst[arr[i+n][j+m]] == k:
                        return 0
                    lst[arr[i+n][j+m]] = k
            k *= (-1)
    return 1

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = check()
    print(f'#{tc}', result)