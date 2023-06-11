# 전기버스

T = int(input())

for test_case in range(1,T+1):
    k, n, m = map(int, input().split())
    idx = list(map(int, input().split()))
    stop = [0]*(n+1)
    for i in range(m):
        stop[idx[i]] = 1

    cnt = 0
    bus = k
    while bus < n:

        # 버스 현재 위치 + 1 ~ 버스 현재 위치 + k : 충전기 유무
        for j in range(bus, bus-k, -1):
            if stop[j]:
                cnt += 1
                bus = j + k 
                break
        else:
            cnt = 0
            break

    print(f'#{test_case} {cnt}')
