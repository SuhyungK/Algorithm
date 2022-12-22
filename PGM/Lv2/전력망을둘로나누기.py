def solution(n, wires):
    graph = defaultdict(list)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)


    def dfs(s, e, visited):
        for x in graph[s]:
            if x != e and x not in visited:
                visited.add(x)
                visited = dfs(x, e, visited)
        return visited

    min_v = 1e9
    for i in sorted(graph):
        for j in graph[i]:
            if i > j:
                continue
            
            # print(dfs(i, j, {i}))
            min_v = min(min_v, abs(n - 2*len(dfs(i, j, {i}))))

    return min_v
    
from collections import defaultdict