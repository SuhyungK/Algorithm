def solution(maps):
    
    N, M = len(maps), len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                si, sj = i, j
            elif maps[i][j] == 'E':
                ei, ej = i, j
    
    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visit[si][sj][0] = 1
    q = [(si, sj, 0)]
    while q:
        r, c, lever = q.pop(0)
        if (r, c) == (ei, ej) and lever == 1:
            return visit[r][c][lever]
            
        for dr, dc in (1, 0), (0, -1), (-1, 0), (0, 1):
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < M and (m:=maps[nr][nc]) != 'X' and not visit[nr][nc][lever]: 
                if m == 'L' and lever == 0:
                    visit[nr][nc][1] = visit[r][c][0] + 1
                    q.append((nr, nc, 1))
                else:
                    visit[nr][nc][lever] = visit[r][c][lever] + 1
                    q.append((nr, nc, lever))
        
    return -1
                

# print(solution(['SOOXL', 'OOOOO', 'OOXXX', 'OOOOO', 'OOOOE']))
print(solution(['SXE', 'OOO', 'OOL']))
"""
SXE
OOO
OOL
"""