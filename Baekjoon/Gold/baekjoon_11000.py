# 강의실 배정

N = int(input())
cls = [list(map(int, input().split())) for _ in range(N)]

cls.sort(key=lambda x: x[1])
i = cnt = 1
while i < N:
    j = 1
    if cls[i-1][1] <= cls[i][0]:
        j += 1
        cnt += 1
    i += j

print(cnt)