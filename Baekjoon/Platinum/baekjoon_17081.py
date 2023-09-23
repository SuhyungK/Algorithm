# RPG Extreme

from collections import defaultdict

def find_start(grid): # 출발 위치 찾기
    for i in range(len(grid)):
        if '@' in grid[i]:
            return i, grid[i].index('@')

def thron(): # 가시 찔리기
    global HP, RESULT, ITEMS, ITEMS_CNT
    HP -= 5+min(1, ITEMS['DX_THRON'])
    if HP <= 0:
        if ITEMS['RE']:
            revival()   
            del ITEMS['RE']
            ITEMS_CNT -= 1
            return 
        RESULT = f'YOU HAVE BEEN KILLED BY SPIKE TRAP..'

def revival(): # 주인공 사망하면 1. 최대 체력 부활, 2. 시작 위치로 이동
    global HP, r, c
    HP = MAX_HP
    r, c = SR, SC

def level_up():
    global HP, MAX_HP, ATT, DEF, EXP, LV
    if EXP >= 5*LV:
        EXP = 0
        LV += 1
        MAX_HP += 5
        ATT += 2
        DEF += 2
        HP = MAX_HP

def boss_battle(r, c, s, w, a, h, e): # 보스 몬스터랑 싸우기, 이기면 게임 종료
    global RESULT, grid, HP, ITEM, ITEMS_CNT, EXP
    att_alpha = 1
    if ITEMS['HU']: # HU 장신구 있으면 최대 체력 회복
        att_alpha = 0 # 첫 공격이 0
        HP = MAX_HP

    h -= max(1, (ATT+W)*max(1, ITEMS['CO'], ITEMS['DX_ATT'])-a)
    while True:
        if h <= 0: # 보스 몬스터가 지면 게임 종료
            RESULT = 'YOU WIN!'
            EXP = EXP+int(e*max(1, ITEMS['EX']))
            HP = min(MAX_HP, HP+ITEMS['HR'])
            level_up()
            return 
        
        HP -= (max(1, w-(DEF+A)))*att_alpha
        if HP <= 0: # 주인공이 진 경우
            grid[r][c] = 'M'
            if ITEMS['RE']: # 부활 가능?
                revival()
                del ITEMS['RE']
                ITEMS_CNT -= 1
                return 
            RESULT = f'YOU HAVE BEEN KILLED BY {s}..'
            return 
        att_alpha = 1

        h -= max(1, (ATT+W)-a)

def battle(r, c, s, w, a, h, e): # 일반 몬스터랑 싸우기
    global RESULT, grid, HP, ITEM, ITEMS_CNT, EXP

    # 주인공의 첫 번째 공격
    h -= max(1, (ATT+W)*max(1, ITEMS['CO'], ITEMS['DX_ATT'])-a)
    
    while True:
        if h <= 0:
            del MONSTER[(r, c)]
            grid[r][c] = '.'
            EXP = EXP+int(e*max(1, ITEMS['EX']))
            HP = min(MAX_HP, HP+ITEMS['HR'])
            level_up()
            return
         
        # 몬스터의 공격
        HP -= max(1, w-(DEF+A))
        if HP <= 0:
            grid[r][c] = '&'
            del MONSTER[(r, c)]
            if ITEMS['RE']:
                revival()
                del ITEMS['RE']
                ITEMS_CNT -= 1
                return
            RESULT = f'YOU HAVE BEEN KILLED BY {s}..'
            return
        
        # 주인공의 공격
        h -= max(1, (ATT+W)*max(1, ITEMS['CO'], ITEMS['DX_ATT'])-a)

def wear_item(t, s):
    global ITEMS, ITEMS_CNT
    # 착용한 장신구가 4개거나 동일한 장신구를 착용중인 경우
    if ITEMS_CNT == 4 or ITEMS[s]:
        return 

    ITEMS_CNT += 1
    if s == 'HR': 
        ITEMS['HR'] = 3
    elif s == 'RE':
        ITEMS['RE'] = 1
    elif s == 'CO':
        ITEMS['CO'] = 2
        if ITEMS['DX_THRON']:
            ITEMS['DX_ATT'] = 3
    elif s == 'EX':
        ITEMS['EX'] = 1.2
    elif s == 'DX':
        ITEMS['DX_THRON'] = -4
        if ITEMS['CO']:
            ITEMS['DX_ATT'] = 3
    elif s == 'HU':
        ITEMS['HU'] = 1
    elif s == 'CU':
        ITEMS['CU'] = 1
    
def open_box(r, c): # 박스 열기
    global W, A
    t, s = BOXES[(r, c)]
    del BOXES[(r, c)]
    
    if t == 'W':
        W = s
    elif t == 'A':
        A = s
    else:
        wear_item(t, s)
    grid[r][c] = '.'

# INIT
HP, MAX_HP, ATT, DEF, EXP, LV, W, A, ITEMS, ITEMS_CNT = 20, 20, 2, 2, 0, 1, 0, 0, defaultdict(int), 0
MOVE = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
MONSTER, BOXES = {}, {}
ACTION = {
    '^': lambda x: thron(),
    'B': lambda x: open_box(*x),
    '&': lambda x: battle(*x, *MONSTER[*x]),
    'M': lambda x: boss_battle(*x, *MONSTER[*x])
}
RESULT = 'Press any key to continue.'

# INPUT
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
direction = input()
K = sum(row.count('&') for row in grid)+1
L = sum(row.count('B') for row in grid)
for _ in range(K):
    r, c, *info = map(lambda x: int(x) if x.isdigit() else x, input().split())
    MONSTER[(r-1, c-1)] = info
for _ in range(L):
    r, c, *ts = map(lambda x: int(x) if x.isdigit() else x, input().split())
    BOXES[(r-1, c-1)] = ts

SR, SC = find_start(grid)
r, c = SR, SC

# GAME_START
turns = 0
for d in direction:
    turns += 1
    dr, dc = MOVE[d]
    if grid[r][c] != '^':
        grid[r][c] = '.'

    if -1<r+dr<n and -1<c+dc<m and grid[r+dr][c+dc] != '#':
        r += dr
        c += dc
    if grid[r][c] != '.':
        ACTION[grid[r][c]]((r, c))

    if grid[r][c] != '^' and not RESULT.startswith('YOU HAVE'):
        grid[r][c] = '@'
        
    if RESULT != 'Press any key to continue.':
        break
else:
    grid[r][c] = '@'

for row in grid:
    print(''.join(row))
print(f"Passed Turns : {turns}")
print("LV :", LV)
print(f"HP : {max(0, HP)}/{MAX_HP}")
print(f"ATT : {ATT}+{W}")
print(f"DEF : {DEF}+{A}")
print(f"EXP : {int(EXP)}/{5*LV}")
# print(ITEMS, ITEMS_CNT, MONSTER)
print(RESULT)