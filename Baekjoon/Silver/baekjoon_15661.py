# 링크와 스타트

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
minV = 1e9
cnt = 0

def score(start, link, i):
    global minV, cnt
    if cnt > 2 ** (N - 1):
        return 

    if i == N:
        if start and link:
            cnt += 1
            sV = lV = 0
            for si in range(len(start)):
                for sj in range(si+1, len(start)):
                    sV += (stats[start[si]][start[sj]] + stats[start[sj]][start[si]])
            for li in range(len(link)):
                for lj in range(li+1, len(link)):
                    lV += (stats[link[li]][link[lj]] + stats[link[lj]][link[li]])
            diff = abs(sV - lV)
            if minV > abs(diff):
                minV =  abs(diff)
            # print(start, link, diff)
        return


    score(start, link, i+1)
    link.remove(i)
    score(start + [i], link, i+1)
    link.append(i)

score([], [i for i in range(N)], 0)

print(minV)