# 이차원 배열과 연산

def arrange(row):
    tmp = {}
    for r in row:
        if r:
            tmp[r] = tmp.get(r, 0) + 1
    
    lst = []
    for row in sorted(list(map(list, zip(tmp.keys(), tmp.values()))), key=lambda x: (x[1], x[0])):
        lst.extend(row)

    return lst[:100]

def Row(arr):
    global r, c
    for i in range(r):
        arr[i] = arrange(arr[i])

    c = max([len(row) for row in arr])
    
    for row in arr:
        row += [0] * (c - len(row))
    
    return arr

def Col(arr):
    global r, c
    arr = list(map(list, zip(*arr)))
    for j in range(c):
        arr[j] = arrange(arr[j])
    
    r = max([len(col) for col in arr])

    for col in arr:
        col += [0] * (r -len(col))

    return list(map(list, zip(*arr)))

def sol(arr):
    time = 0
    if -1<R<r and -1<C<c and arr[R][C] == K:
        print(time)
        return 
    while True:
        if r >= c:
            arr = Row(arr)
        else:
            arr = Col(arr)
        time += 1
        if -1<R<r and -1<C<c and arr[R][C] == K:
            print(time)
            break
        if time >= 100:
            print(-1)
            break

R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
R -= 1; C-= 1
r = c = 3

if __name__ == '__main__':
    sol(arr)