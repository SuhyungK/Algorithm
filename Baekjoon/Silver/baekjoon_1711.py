# S1 직각삼각형 

import sys
input = sys.stdin.readline

N = int(input())
tri = [tuple(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            abc = [
                (tri[i][0] - tri[j][0]) ** 2 + (tri[i][1] - tri[j][1]) ** 2,
                (tri[j][0] - tri[k][0]) ** 2 + (tri[j][1] - tri[k][1]) ** 2, 
                (tri[k][0] - tri[i][0]) ** 2 + (tri[k][1] - tri[i][1]) ** 2  
            ]
            # abc.sort()
            if abc[2] == abc[0] + abc[1] or abc[0] == abc[1] + abc[2] or abc[1] == abc[0] + abc[2]:
                cnt += 1
print(cnt)