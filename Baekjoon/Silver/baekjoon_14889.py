# 스타트와 링크

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
limit = N // 2
cnt_limit = 1
for i in range(1, limit+1):
    cnt_limit = cnt_limit * (i+limit) // i
cnt_limit //= 2
cnt, min_diff = 0, 1e9

def make_team(start, i):
    global cnt, min_diff
    if cnt >= cnt_limit:
        return 

    if len(start) == limit:
        cnt += 1
        link = []
        for k in range(N):
            if k not in start:
                link.append(k)
        sV = lV = 0
        for _i in range(limit):
            for _j in range(_i, limit):
                sV += (arr[start[_i]][start[_j]] + arr[start[_j]][start[_i]])
                lV += (arr[link[_i]][link[_j]] + arr[link[_j]][link[_i]])
        min_diff = min(min_diff, abs(sV - lV))

    for j in range(i, N):
        if j not in start:
            make_team(start + [j], j+1)

make_team([], 0)
print(min_diff)