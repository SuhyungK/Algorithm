# 어항 정리

# 회전
def rotate(arr):
    return list(map(list, zip(*arr[::-1])))[::-1]

# 가장 작은 물고기의 어항에 1추가
def minimum_fish(arr):
    min_v = min(arr[0])
    for i in range(len(arr[0])):
        if arr[0][i] == min_v:
            arr[0][i] += 1
    return arr

# 어항 떼어내서 돌리기 
def detach(arr, r, k):
    tmp = []
    for i in range(r-1):
        tmp.append(arr.pop())
    tmp.append(arr[0][:k])
    arr[0] = arr[0][k:]
    return tmp, arr

# 첫 번째 어항 쌓기
def stack(arr):
    arr.append([arr[0].pop(0)])
    
    while True:
        r, c, k = len(arr), len(arr[0]), len(arr[-1])
        if c-k<r:
            break
        tmp, arr = detach(arr, r, k)
        arr.extend(rotate(tmp))
    return arr

# 물고기 수 조절
def fish_control(arr):
    n = len(arr)
    tmp = [[0]*len(arr[i]) for i in range(n)]

    for i in range(n):
        m = len(arr[i])
        for j in range(m):
            for ni, nj in (i-1, j), (i, j+1):
                if not(-1<ni<n and -1<nj<m):
                    continue
                
                mod = abs(arr[i][j] - arr[ni][nj])//5
                if mod < 0:
                    continue
                if arr[i][j] > arr[ni][nj]:
                    tmp[ni][nj] += mod
                    tmp[i][j] -= mod
                else:
                    tmp[i][j] += mod
                    tmp[ni][nj] -= mod
    
    for i in range(n):
        for j in range(len(arr[i])):
            arr[i][j] += tmp[i][j]
    return arr

# 일렬로 만들기
def make_row(arr):
    tmp, lst = detach(arr, len(arr), len(arr[-1]))
    arr = []
    for row in rotate(tmp)[::-1]:
        arr.extend(row)
    arr.extend(*lst)
    return [arr]

# 공중 부양 
def levitation(arr):
    for i in range(2):
        tmp = []
        k = len(arr[0])//2
        for j in range(len(arr)-1, -1, -1):
            tmp.append(arr[j][:k][::-1])
            arr[j] = arr[j][k:]
        arr.extend(tmp)
    return arr

n, k = map(int, input().split())
arr = [list(map(int, input().split()))]
count = 0

while True:
    if max(arr[0]) - min(arr[0]) <= k:
        print(count)
        break
    
    arr = make_row(fish_control(levitation(make_row(fish_control(stack(minimum_fish(arr)))))))
    count += 1