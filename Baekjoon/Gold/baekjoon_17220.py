N, M = map(int, input().split())

pos_pub, drugs = ['O'] * N, {}
for _ in range(M):
    f, b = map(lambda x: ord(x) - 65, input().split())
    pos_pub[b]= '.'
    if drugs.get(b):
        drugs[b].append(f)
    else:
        drugs[b] = [f]

real_pub = input().split()
for real in real_pub[1:]:
    real = ord(real) - 65
    pos_pub[real] = 'X'

def dfs(s):
    if pos_pub[s] in ('O', 'X'):
        return pos_pub[s] == 'O'
    
    for e in drugs[s]:
        if dfs(e):
            pos_pub[s] = 'O'
            return 1
    pos_pub[s] = 'X'
    return 0

ans = 0
for s in range(N):
    if pos_pub[s] == '.':
        ans += dfs(s)

print(ans)