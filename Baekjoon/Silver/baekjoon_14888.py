# 연산자 끼워넣기

def calc(res, k, p, m, t, d):
    global max_res, min_res
    if k == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return 
    if p:
        calc(res+nums[k], k+1, p-1, m, t, d)
    if m:
        calc(res-nums[k], k+1, p, m-1, t, d)
    if t:
        calc(res*nums[k], k+1, p, m, t-1, d)
    if d:
        calc(int(res/nums[k]), k+1, p, m, t, d-1)
      
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_res, min_res = -1e13, 1e13
calc(nums[0], 1, *ops)
print(max_res)
print(min_res)


print(int(-4/3))