# 호석이 두 마리 치킨
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
bldn = [[] for _ in range(N)]
dis = [[0] * N for _ in range(N)]

# 입력값 받기
for _ in range(M):
    i, j = map(lambda x: int(x) -1, input().split())
    bldn[i].append(j)
    bldn[j].append(i)

# 1 ~ N까지 모든 치킨집 돌면서 각각의 거리 2차원 배열 dis에 저장
for i in range(N):
    q = [i]
    while q:
        s = q.pop(0)
        for e in bldn[s]:
            if i != e and not dis[i][e]:
                dis[i][e] = dis[i][s] + 1
                q.append(e)
        print(dis)

# ans_cks: 건물 조합(tuple)
# ans_time: 왕복 시간의 합
# 이중 for문으로 건물 조합 구하고 그 건물 두개랑 나머지 건물 둘 사이의 거리 중에서 최소값의 합을 비교해서 더 작을 때만 저장
ans_cks = []
ans_time = 1e9
for ck1 in range(N-1):
    for ck2 in range(ck1+1, N):
        if ans_time > (temp:=sum([min(dis[ck1][c], dis[ck2][c]) for c in range(N)])):
            ans_time, ans_cks = temp, (ck1+1, ck2+1)

print(*ans_cks, ans_time*2)