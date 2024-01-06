# 원판 돌리기

"""
1. 원판 회전
2. 원판에 남아 있는 수 
    2-1. 남아 있으면 : 서로 인접하면서 같은 수 모두 0
    2-2. x : 평균 구하고 평균보다 큰 수 -1, 작은 수 +1
"""

def rotate(i, d, k):
    k %= M
    if d == 0:
        k *= -1
    circle[i] = circle[i][k:] + circle[i][:k] 

def find(t): # 인접한 수 찾기
    remove_list = list()

    for i in range(N):
        for j in range(M):
            if visited[i][j] != t and circle[i][j]:
                visited[i][j] = t
                tmp = [(i, j)]
                queue = [(i, j)]
                while queue:
                    ii, jj = queue.pop(0)
                    for di, dj in (ii+1, jj), (ii-1, jj), (ii, (jj+1)%M), (ii, (jj-1)%M):
                        if di < 0 or dj < 0 or di >= N or dj >= M or visited[di][dj] == t or circle[di][dj] != circle[ii][jj]:
                            continue
                    
                        visited[di][dj] = t
                        tmp.append((di, dj))
                        queue.append((di, dj))
                if len(tmp) > 1:
                    remove_list.extend(tmp[:])

    return remove_list

def remove(remove_list):
    global total_sum
    for i, j in remove_list:
        total_sum[0] -= circle[i][j]         
        total_sum[1] -= 1        
        circle[i][j] = 0

def avg():
    avg_sum = total_sum[0] / total_sum[1]
    for i in range(N):
        for j in range(M):
            if circle[i][j] == 0:
                continue
            
            if circle[i][j] > avg_sum:
                circle[i][j] -= 1
                total_sum[0] -= 1
            elif circle[i][j] < avg_sum:
                circle[i][j] += 1
                total_sum[0] += 1

N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
total_sum = [sum([sum(row) for row in circle]), N*M]
visited = [[0] * M for _ in range(N)]

for t in range(1, T+1):
    x, d, k = map(int, input().split())

    for i in range(x, N+1, x):
        rotate(i-1, d, k)
    
    remove_list = find(t)
    if len(remove_list) != 0:
        remove(remove_list)
    else:
        avg()
    
    if total_sum[1] == 0:
        break

print(total_sum[0])