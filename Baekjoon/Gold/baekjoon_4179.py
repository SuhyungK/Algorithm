# 불!

def find_JF():
    global J, F
    for i in range(R):
        for j in range(C):
            if MAZE[i][j] == 'F':
                F.append((i, j))
            elif MAZE[i][j] == 'J':
                J = [i, j]

def exodus(J, fq):
    jr, jc = J
    MAZE[jr][jc] == 'J' # 지훈이가 방문했던 곳을 또 방문하지 않도록 하기 위해서
    jq = [(jr, jc)]
    time = 1
    # 지훈이가 이동할 수 있는 지역이 있나?
    while jq:

        # 불이 먼저 확산되고
        l = len(fq)
        for fr, fc in fq[:l]:
            for nr, nc in (fr-1, fc), (fr+1, fc), (fr, fc-1), (fr, fc+1):
                if nr<0 or nc<0 or nr>=R or nc>=C or MAZE[nr][nc] == '#':
                    continue
                
                fq.append((nr, nc))
                MAZE[nr][nc] = '#'
        fq = fq[l:]

        # 불과 벽, 이미 지훈이가 방문한 공간을 제외하고 지훈이가 이동할 수 있는 방향으로 확산
        # 더 갈 수 있는 곳이 없다면 ....
        _l = len(jq)
        for jr, jc in jq[:_l]:
            for _nr, _nc in (jr+1, jc), (jr-1, jc), (jr, jc+1), (jr, jc-1):
                if _nr<0 or _nc<0 or _nr>=R or _nc>=C:
                    return time
                
                if MAZE[_nr][_nc] != '.':
                    continue
                
                MAZE[_nr][_nc] = 'J'
                jq.append((_nr, _nc))

        jq = jq[_l:]

        print()
        for row in MAZE:
            print(*row)
        time += 1

    return 'IMPOSSIBLE'

R, C = map(int, input().split())
MAZE = [list(input()) for _ in range(R)]
J, F = [], []

find_JF()
print(exodus(J, F))