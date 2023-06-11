# 전구

def sol(order, b, c):
    global state
    if order == 1:
        state[b] = c
    elif order == 2:
        for i in range(b, c+1):
            state[i] = 0 if state[i] == 1 else 1
    elif order == 3:
        state[b:c+1] = [0]*(c-b+1)
    else:
        state[b:c+1] = [1]*(c-b+1)

N, M = map(int, input().split())
state = [0]+list(map(int, input().split()))

for _ in range(M):
    Input = map(int, input().split())
    sol(*Input)
    
print(*state[1:])