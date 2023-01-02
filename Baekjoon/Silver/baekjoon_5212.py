# BOJ S2 지구 온난화

R, C = map(int, input().split())
sea = [list(input()) for _ in range(R)]

# 사라질 섬 찾기
remove_island = []
for r in range(R):
    for c in range(C):
        if sea[r][c] == 'X':
            not_sea = 0
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc  = r + dr, c + dc
                if -1 < nr < R and -1 < nc < C and sea[nr][nc] == 'X':
                    not_sea += 1
            if 4 - not_sea >= 3:
                remove_island.append((r, c))

# 섬 사라지게 하기
for ris in remove_island:
    r, c = ris
    sea[r][c] = '.'

# 한 행 또는 한 열이 전부 바다인 경우 걍 삭제하기
# 가운데가 아니라 각 모서리부분의 경우만 삭제해야함

# 행의 아래부터 삭제
for i in range(R-1, -1, -1):
    # 도중에 섬인 부분이 나타나면 break
    if ''.join(sea[i]) != '.' * C:
        break
    sea.pop(i)

# 다시 행의 맨위쪽부터 시작
_p = 0
for _i in range(len(sea)):
    if ''.join(sea[_i-_p]) != '.' * C:
        break
    sea.pop(_i-_p)
    _p += 1

# 회전시켜서 열 검사(행과 마찬가지)
n_R = len(sea)
n_sea = list(map(list, zip(*sea)))
for _i in range(C-1, -1, -1):
    if ''.join(n_sea[_i]) != '.' * n_R:
        break
    n_sea.pop(_i)

p = 0
for i in range(len(n_sea)):
    if ''.join(n_sea[i-p]) != '.' * n_R:
        break
    n_sea.pop(i-p)
    p += 1

sea = list(map(list, zip(*n_sea)))
for row in sea:
    print(''.join(row))