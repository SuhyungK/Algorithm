# 주사위 굴리기

def sol(dice):
    global x,y
    res, idx = [], 0
    while idx < K:
        odr = orders[idx]
        idx += 1
        
        if odr == '1':
            if y+1>=M:
                continue
            y += 1
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif odr == '2':
            if 0>y-1:
                continue
            y -= 1
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif odr == '3':
            if 0>x-1:
                continue
            x -= 1
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif odr == '4':
            if x+1>=N:
                continue
            x += 1
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if MAP[x][y] == '0':
            MAP[x][y] = dice[-1]
        else:
            dice[-1], MAP[x][y] = MAP[x][y], '0'

        res.append(dice[0])
    return res

N, M, x, y, K = map(int, input().split())
MAP = [list(input().split()) for _ in range(N)]
orders = list(input().split())
dice = ['0']*6

res = sol(dice)
print('\n'.join(res))