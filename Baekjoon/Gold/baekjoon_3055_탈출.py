r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

water, beaver = [], []
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append([i, j])
        elif arr[i][j] == 'S':
            arr[i][j] = 1
            beaver = [[i, j]]

def bfs(water, beaver):
    while beaver:
        new_water = []
        for wr, wc in water:
            for i in range(4):
                nr, nc = wr + dr[i], wc + dc[i]
                if -1 < nr < r and -1 < nc < c and arr[nr][nc] == '.':
                    arr[nr][nc] = '*'
                    new_water.append([nr, nc])
        water = new_water

        new_start = []
        for br, bc in beaver:
            for i in range(4):
                nr, nc = br + dr[i], bc + dc[i]
                if -1 < nr < r and -1 < nc < c and arr[nr][nc] in ['D', '.']:
                    if arr[nr][nc] == 'D':
                        return arr[br][bc] 
                    arr[nr][nc] = arr[br][bc] + 1
                    new_start.append([nr, nc])
        beaver = new_start
    return 'KAKTUS'

print(bfs(water, beaver))