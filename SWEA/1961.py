T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]

    print(f'#{tc}')
    rows = [[] for _ in range(n)]
    for _ in range(3):
        arr = list(map(list, zip(*arr[::-1])))
        for i in range(n):
           	rows[i].append(arr[i])

    for row in rows:
        for r in row:
            print(''.join(r), end=' ')
        print()