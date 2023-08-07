# 숨바꼭질 2

N, K = map(int, input().split())

def sol():
    if N >= K:
        return N-K, 1

    queue = [N]
    time = 0
    visited = [0]*100001
    visited[N] = 1
    while queue:
    
        new_q = []
        for x in queue:
            for y in (x-1, x+1, 2*x):
                if y<0 or y>100000 or visited[y]:
                    continue

                new_q.append(y)

        time += 1
        if K in new_q:
            return time, new_q.count(K)
    
        for x in new_q:
            visited[x] = 1
        queue = new_q[:]

result = sol()
print('\n'.join(map(str, result)))