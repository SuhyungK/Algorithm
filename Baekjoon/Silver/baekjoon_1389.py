# 케빈 베이컨의 6단계 법칙

n, m = map(int, input().split())

arr = [[100000]*n for _ in range(n)]

# 입력값 초기화
for _ in range(m):
    a, b = map(int,input().split())
    arr[a-1][b-1] = arr[b-1][a-1] = 1

for i in range(n):
    arr[i][i] = 0
    
# 플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

# 최소값 찾기
print(arr.index(min(arr, key=sum))+1)
# mv, mv_idx = 1e13, 0
# for idx, row in enumerate(arr,1):
#     if sum(row)<mv:
#         mv,mv_idx = sum(row), idx

# print(mv_idx)