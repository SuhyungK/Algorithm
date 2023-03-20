# 마약 수사대

N, M = map(int, input().split())

# 마약의 원산지를 찾아서 먼저 'O' 표시를 하고
# 검거된 마약 공급처들을 'X' 표시한 뒤
# 모든 마약 공급처를 돌면서 타고 올라가서 'O'를 한 번이라도 만나면 True
# 끝날때까지 한 번도 못 만나면 False
# 밑에서부터 위로 올라가는 구조로 연결

# 첨에 일단 다 'O'로 표시하고 돌면서 한 군데라도 마약 공급받는데가 있으면 '.'
"""
이런식으로 나오게 하기
['O', 'X', 'X', 'O', '.', '.', '.', '.', '.', '.', '.']
['O', 'X', 'X', 'O', 'O', '.', '.', '.', '.', '.', '.']
['O', 'X', 'X', 'O', 'O', 'X', '.', '.', '.', '.', '.']
['O', 'X', 'X', 'O', 'O', 'X', 'O', '.', '.', '.', '.']
['O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', '.', '.', '.']
['O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', '.', '.']
['O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'X', '.']
['O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X']
"""
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