# 원상 복구 (small)

N, K = map(int, input().split())
S = [0]+list(map(int, input().split()))
D = list(map(int, input().split()))

idx, L = 0, len(S)
while idx < K:
    tmp = [0]*L

    for i, s in enumerate(S[1:]):
        tmp[D[i]] = s
    
    S = tmp[:]
    idx += 1

print(*S[1:])