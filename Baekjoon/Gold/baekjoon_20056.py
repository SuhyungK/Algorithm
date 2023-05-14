import sys
input = sys.stdin.readline

# 이동
def move(N):
    new_fireball = {}
    global fireball
    
    for rc, msd in fireball.items():
        r, c = rc
        m, s, d = msd
        for i in d:
            dr, dc = DIR[i]
            nr = (r+dr*s)%N
            nc = (c+dc*s)%N
            if new_fireball.get((nr, nc)):
                new_fireball[(nr, nc)].append([m, s, i])
            else:
                new_fireball[(nr, nc)] = [[m, s, i]]

    fireball = new_fireball

def find_next_dir(d_lst):
    flag = d_lst[0] % 2
    for d in d_lst[1:]:
        if d % 2 != flag:
            return 1, 3, 5, 7
    return 0, 2, 4, 6

# 파이어볼 합치기
def merge_fireball():
    global fireball
    key_lst = fireball.keys()

    new_fireball = {}
    for key in key_lst:
        fire_lst = fireball[key]

        if len(fire_lst) <= 1:
            m, s, d = fireball[key][0]
            new_fireball[key] = [m, s, [d]]
            continue

        total_m = sum((b[0] for b in fire_lst)) // 5
        total_s = sum((b[1] for b in fire_lst)) // len(fire_lst)
        d_lst = [b[2] for b in fire_lst]
        # m_lst, s_lst, d_lst = list(map(list, zip(*fire_lst)))
        # total_m, total_s = sum(m_lst) // 5, sum(s_lst) // len(s_lst)
        if total_m == 0:
            continue
        
        new_fireball[key] = [total_m, total_s, find_next_dir(d_lst)]

    fireball = new_fireball

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    fireball = {}
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball[(r-1, c-1)] = [m, s, [d]]

    DIR = {
        0: (-1, 0),
        1: (-1, 1),
        2: (0, 1),
        3: (1, 1),
        4: (1, 0),
        5: (1, -1),
        6: (0, -1),
        7: (-1, -1)
    }
    
    for _ in range(K):
        move(N)
        merge_fireball()

    res = 0
    for m, _, d in fireball.values():
        res += m * len(d)

    print(res)