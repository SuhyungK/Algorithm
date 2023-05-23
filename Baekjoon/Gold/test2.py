# 56ms
# 각 도시별 union을 파악한 뒤
# 모든 도시가 여행 가능하다면 하나의 union일 것이므로
# 이를 통해 여행 가능 여부를 판단


def find(x):
    if rep[x] != x:
        return find(rep[x])
    return x

'''
다른 버전의 find 함수 => 시간 복잡도 동일

def find(x):
    while x != rep[x]:
        x = rep[x]
    return x
'''

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        rep[y] = x
    else:
        rep[x] = y

'''
다른 버전의 union 함수 => 시간 더 빠름
def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        rep[y] = x
    else:
        rep[x] = y
'''
        
N = int(input()); M = int(input())
rep = [ n for n in range(N+1)] # rep -> root

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j]:
            if find(i+1) != find(j+1):
                union(i+1, j+1)

trip = list(map(int, input().split()))
unions = set()
print(rep)
for i in trip:
    x = find(i)
    unions.add(x)
    if len(unions) > 1:
        print('NO')
        break
else:
    print('YES')
