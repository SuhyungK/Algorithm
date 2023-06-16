# 폴더 정리(small)

def dfs(path):
    global ans
    ans[path] = [set(), 0]

    if file.get(path):
        ans[path][0].update(file[path][0])
        ans[path][1] += len(file[path][0])
        for sub in file[path][1]:
            _type, cnt = dfs(sub)
            ans[path][0].update(_type)
            ans[path][1] += cnt

    return ans[path][0], ans[path][1]
    

file = {}
N, M = map(int, input().split())

for _ in range(N+M):
    p, f, c = input().split()

    if file.get(p):
        file[p][int(c)] += [f]
    else:
        file[p] = [[], []]
        file[p][int(c)] += [f]

ans = {}
dfs('main')

print(ans)
Q = int(input())
for _ in range(Q):
    path = input().split('/')[-1]
    print(len(ans[path][0]), ans[path][1])