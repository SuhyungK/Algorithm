# 거짓말

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y
            
N, M = map(int, input().split())
T, *truth = map(int, input().split())
root = list(range(N+1))
party = []

for _ in range(M):
    P, *ppl = map(int, input().split())
    party.append(ppl)

def sol():
    if not truth:
        return M
    
    # 진실을 아는 사람들 집합으로 묶기
    for i in range(T-1):
        union(truth[i], truth[i+1])

    # 각 파티에서 만난 사람들 하나의 집합으로 묶기
    for ppl in party:
        for j in range(len(ppl)-1):
            if find(ppl[j]) != find(ppl[j+1]):
                union(ppl[j], ppl[j+1])
                print(root)

    # 어떤 파티에 가서 과장된 얘기를 해도 되는지 확인
    ans = 0
    for ppl in party:
        if find(ppl[0]) != find(truth[0]):
            ans += 1

    return ans

print(sol())