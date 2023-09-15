# 넴모넴모 (Easy)

def possible(r, c):
    count = 0
    if r>0 and arr[r-1][c]:
        count += 1
    if c>0 and arr[r][c-1]:
        count += 1
    if r>0 and c>0 and arr[r-1][c-1]:
        count += 1
    return count != 3

def nemo(i):
    global nemo, result
    if i == n*m:
        result += 1
        return 
    
    r, c = divmod(i, m)
    if possible(r, c):
        arr[r][c] = 1
        nemo(i+1)
        arr[r][c] = 0
    nemo(i+1)

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

result = 0
nemo(0)
print(result)