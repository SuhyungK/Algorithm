# 두 용액

N = int(input())
properties = list(map(int, input().split()))
properties.sort()

for i in range(N):
    now = properties[i]
    left, right = i+1, N - 1
    min_sum = float('inf')
    while left <= right:
        m = (left + right) // 2
        if abs(now - properties[m]) >= min_sum:
            left = m + 1
        else:
            min_sum = abs(now - properties[m])
            right = m - 1
print(min_sum)

arr = list(map(int, input().split()))
arr.sort()

l, r = 0, N-1
cur_res, min_dif = (), float('inf')
while l < r:
    cur_sum = arr[l] + arr[r]
    if abs(cur_sum) < min_dif:
        min_dif = abs(cur_sum)
        cur_res = (arr[l], arr[r])
    
    if cur_sum > 0:
        r -= 1
    else:
        l += 1
        
print(*cur_res)
