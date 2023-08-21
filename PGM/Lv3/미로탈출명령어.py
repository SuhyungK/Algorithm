def solution(n, m, x, y, r, c, k):
    # d l r u
    dist = abs(r-x) + abs(c-y)
    if dist>k or (k-dist)%2:
        return 'impossible'
    
    # 최단거리 : 탈출 위치와 현재 위치 사이의 거리... 가능한 방향...
    d1 = max(r-x, 0)
    l1 = max(y-c, 0)
    r1 = max(c-y, 0)
    u1 = max(x-r, 0)
    
    # 잉여거리 : 출발이든 탈출이든 둘 중 어느 위치에서든간에 최단거리를 제외하고 갈 수 있는 남은 거리
    # 아래와 왼만 고려
    d2 = min(n-x, n-r)
    l2 = min(y-1, c-1)
    
    # 잉여경로
    rem = k - dist
    d_rem = min(rem//2, d2)
    rem = max(rem-d2*2, 0)
    
    l_rem = min(rem//2, l2)
    rem = max(rem-l2*2, 0)
    
    rl_rem = max(rem//2, 0)
    
    # 경로구하기
    route = 'd'*(d1+d_rem) + 'l'*(l1+l_rem) + 'rl'*rl_rem + 'r'*(r1+l_rem) + 'u'*(u1+d_rem)
    
    return route