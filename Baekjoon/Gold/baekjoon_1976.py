# G4 여행 가자

def trip():
    for i in range(N-1):
        s, e = plan[i], plan[i+1]
        q = [s]
        visit[s] = s
        plan[i] = 0
        while q:
            d = q.pop(0)
            for j in city[d]:
                if visit[j] != s:
                    q.append(j)
                    visit[j] = s
    if any(plan[:-1]):
        return 'NO'
    return 'YES'


import sys
sys.stdin = open('input.txt')

N, M = int(input()), int(input())
city = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) -1, input().split()))
visit = [-1] * N

# 모든 여행지를 다 가보게 되면 종료
print(trip())