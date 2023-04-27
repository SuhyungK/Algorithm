# 두 용액

N = int(input())
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