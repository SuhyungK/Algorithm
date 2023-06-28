# 텀 프로젝트

for tc in range(int(input())):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)

    check = 0
    for idx in range(1, N+1):
        if visited[idx]:
            continue

        # 이미 방문된 곳이 있다면 탐색 종료
        cur = idx
        while not visited[cur]:
            visited[cur] = idx
            cur = graph[cur]
        
        # 이 탐색의 시작 숫자 ~ 사이클의 시작 숫자 사이의 개수 세기
        # 만약 시작 숫자 = 사이클의 시작 숫자라면 0개가 된다
        next = idx
        while next != cur:
            check += 1
            next = graph[next]
        
    print(check)