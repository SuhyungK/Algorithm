# 경사로 40ms

import sys
input = sys.stdin.readline

def fore(row, s, n, ramp): # 행, 시작점 값
    for t in range(L):
        next = s+t
        if next>=N: 
            return False
        
        if row[next] != n or ramp[next]:
            return False
        ramp[next] = True
    
    return True


def back(row, s, n, ramp):
    for t in range(1, L+1):
        prev = s-t
        if prev<0:
            return False
        
        if row[prev] != n or ramp[prev]:
            return False
        ramp[prev] = True
    
    return True

def main(arr):
    global ans
    for row in arr:
        t, next = row[0], 1
        ramp = [False]*N
        while next < N:
            if t == row[next]:
                next += 1
                continue

            gap = t-row[next]
            if gap > 1 or gap < -1:
                break

            if gap == -1:
                if not back(row, next, t, ramp):
                    break
            
            elif gap == 1:
                if not fore(row, next, t-1, ramp):
                    break
                next += (L-1)
                
            t = row[next]
        else:
            # print(row)
            ans += 1

N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ROTATE_MAP = list(map(list, zip(*MAP))) 
ans = 0

main(MAP)
main(ROTATE_MAP)
print(ans)