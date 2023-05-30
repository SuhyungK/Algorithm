def calc(k, res):
    global max_res, min_res
    if k == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return 
    
    prev = -1
    for i in range(N-1):
        if not check[i] and prev != op[i]:
            check[i] = True
            calc(k+1, arith[op[i]](res, nums[k]))
            prev = op[i]
            check[i] = False

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
check = [False]*N

op = []
for i, o in enumerate(ops):
    op.extend([i]*o)
op.sort()

arith = {
    0: lambda x, y : int(x) + int(y),
    1: lambda x, y : int(x) - int(y),
    2: lambda x, y : int(x) * int(y),
    3: lambda x, y : -(abs(int(x)) // int(y)) if int(x) < 0 else int(x) // int(y)
}

max_res, min_res = -float('inf'), float('inf')
calc(1, nums[0])
print(max_res)
print(min_res)