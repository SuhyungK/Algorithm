# 게란으로 계란치기

def is_left(now, dura):
    for i in range(n):
        if i != now and dura[i] > 0:
            return True
    return False

def dfs(now):
    global answer
    if now == n:
        answer = max(answer, sum(1 for i in range(n) if dura[i] <= 0))
        return 
    
    if dura[now] <= 0:
        dfs(now+1)
        return 

    if not is_left(now, dura):
        dfs(now+1)
        return 
    
    for i in range(n):
        if i == now or dura[i]<=0:
            continue
        dura[i] -= weight[now]
        dura[now] -= weight[i]
        dfs(now+1)
        dura[i] += weight[now]
        dura[now] += weight[i]

n = int(input())
dura, weight = list(map(list, zip(*[map(int, (input().split())) for _ in range(n)])))

answer = 0
dfs(0)
print(answer)