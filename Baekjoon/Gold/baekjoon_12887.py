# # 경로 게임

# n = int(input())
# route = [list(input()) for _ in range(2)]

# res = 2*n - sum(route, []).count('#')

# def bfs(r, c):
#     cnt = 0
#     while 1:
#         cnt += 1
#         if c == n-1:
#             return cnt
        
#         if c+1 < n and route[r][c+1] == '.':
#             c += 1
#         elif r == 0:
#             r += 1
#         elif r == 1:
#             r -= 1

# min_cnt = 2*n    
# if route[0][0] == '.':
#     min_cnt = min(min_cnt, bfs(0, 0))

# if route[1][0] == '.':
#     min_cnt = min(min_cnt, bfs(1, 0))

# print(res - min_cnt)


M = int(input())
Map = []
for _ in range(2):
    Map.append(list(input()))

def isBlack(_):
    if _ == '#': return True
    return False

def getLength(i,j): #시작 위치 [i][j]
    length = 1
    while j != M:
        if isBlack(Map[i][j]):
            if i == 1:
                i = 0
            else:
                i = 1
            if j != 0:
                length += 1
        else:
            j += 1
            length += 1
        print(i, j)
    return length-1 #인덱스 초과됐으므로 -1


length = min(getLength(0,0), getLength(1,0))
black = Map[0].count('#') +Map[1].count('#')
print((M*2)-(length+black))