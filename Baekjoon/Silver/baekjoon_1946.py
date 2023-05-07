test_case = int(input())
for t in range(test_case):
    n = int(input())
    rank = [0] * (n+1)
    for _ in range(n):
        i, a = map(int, input().split())
        rank[i] = a

    select = 1
    top_rank = rank[1]
    for j in range(2, n+1):
        if top_rank > rank[j]:
            select += 1
            top_rank = rank[j]
    
    print(select)

