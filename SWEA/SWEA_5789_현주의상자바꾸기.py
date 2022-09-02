T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    box = [0] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for k in range(l, r+1):
            box[k-1] = i

    print(f'#{tc}',*box)
