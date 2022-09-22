T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())), reverse=1)
    T = sorted(list(map(int, input().split())), reverse=1)

    w = i = j = 0       # i : 화물(W) 인덱스 / j : 트럭(T) 인덱스
    while i < N:        # 화물을 다 옮기면 끝
        if W[i] <= T[j]:# 트럭에 화물을 옮길 수 있으면 다음 화물, 트럭으로
            w += W[i]
            j += 1
            if j == M:  # 트럭이 다 차면 끝
                break
        i += 1          # 트럭에 화물을 옮길 수 없으면 다음 화물로 비교

    print(f'#{tc}', w)