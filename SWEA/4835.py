# 구간합

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = min_sum = 0
    for a in arr:
        min_sum += a

    for i in range(n-m+1):
        sum = 0
        for j in range(i,i+m):
            sum += arr[j]
        max_sum = sum if max_sum < sum else max_sum
        min_sum = sum if min_sum > sum else min_sum

    print(f'#{test_case} {max_sum - min_sum}')
