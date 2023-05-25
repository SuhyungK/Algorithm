# 청소년 상어

def fist_move():
    for n in range(1, 17):
        x, y, dir = fish_lst[n]

        for d in range(1, 9):
            nx, ny = DX[dir+d], DY[dir+d]
            if nx<0 or ny<0 or nx>=4 or ny>=4:
                continue

        

def shark_move():
    pass

DX = (-1, -1, 0, 1, 1, 1, 0, -1)
DY = (0, -1, -1, -1, 0, 1, 1, 1) 
fish_lst = {}
fish_arr = {}
for i in range(4):
    row = tuple(map(int, input().split()))
    for j in range(0, 8, 2):
        fish_lst[row[j]] = (i, j)
        fish_arr[(i, j)] = row[j+1]

print(fish_lst)
print(fish_arr)