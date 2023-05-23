# 여행 가자

N, M = int(input()), int(input())
city = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) -1, input().split()))
uni = [0] * N

