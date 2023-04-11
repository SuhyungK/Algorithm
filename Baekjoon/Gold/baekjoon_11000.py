# 강의실 배정

N = int(input())
cls = [list(map(int, input().split())) for _ in range(N)]
cls.sort(key=lambda x: x[1])
v = [0] * N

cnt = 0
for i in range(N):
    if not v[i]:
        v[i] = 1
        next = i+1
        cnt += 1
        while next < N:
            if cls[i][1] <= cls[next][0]:
                v[next] = 1
                i, next = next, next+1
            else:
                next += 1
print(cnt)