# 로또 

def dfs(k, S, comb, result):
    if len(comb) == 6:
        result.append(comb[:])
        return result
    
    for i in range(k, len(S)):
        comb.append(S[i])
        result = dfs(i+1, S, comb, result)
        comb.remove(S[i])
    return result

while True:
    k, *S = list(map(int, input().split()))
    if k == 0:
        break
    
    comb = dfs(0, S, [], [])
    for row in comb:
        print(*row)
    print()