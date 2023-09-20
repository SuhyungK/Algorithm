# 스도쿠

# 스도쿠

def check_row(x):
    return {k for k in range(1, 10) if k not in arr[x]}

def check_col(y):
    return {k for k in range(1, 10) if k not in [arr[x][y] for x in range(9)]}

def check_rect(x, y):
    res = set(range(1, 10))
    for i in range(3*x, 3*x+3):
        for j in range(3*y, 3*y+3):
            res -= {arr[i][j]}
    return res

def find_blank(arr):
    blank = dict()
    for i in range(9):
        for j in range(9):
            if not arr[i][j]:
                blank[(i, j)] = rows[i]&cols[j]&rects[3*(i//3)+j//3]
    return blank

def check(x, y, k):
    return k in rows[x]&cols[y]&rects[3*(x//3)+y//3]
    
def dfs(i, keys, arr):
    if i == len(keys):
        return True
        
    x, y = keys[i]
    for k in blank[(x, y)]:
        if check(x, y, k):
            rows[x].remove(k)
            cols[y].remove(k)
            rects[3*(x//3)+y//3].remove(k)
            if dfs(i+1, keys, arr):
                arr[x][y] = k
                return True
            rows[x].add(k)
            cols[y].add(k)
            rects[3*(x//3)+y//3].add(k)
    return False

arr = [list(map(int, input())) for _ in range(9)]
rows = [check_row(i) for i in range(9)]
cols = [check_col(j) for j in range(9)]
rects = [check_rect(i, j) for i in range(3) for j in range(3)]
blank = find_blank(arr)
keys = list(blank.keys())

dfs(0, keys, arr)
for row in arr:
    print(''.join(map(str, row)))
