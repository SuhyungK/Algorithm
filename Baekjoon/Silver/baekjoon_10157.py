# 자리 배정

def arrange_seat(C, R, K):
    x, y = 1, 1
    u = 1

    if K - R < 0:
        return 1, K
    else:
        K -= R
        y += (R-1)

    while 1:
        C -= 1

        if K-C > 0:
            K -= C
            x += u * C
        else:
            x += u * K
            return x, y
        
        u *= (-1)
        R -= 1

        if K-R > 0:
            K -= R
            y += u * R
        else:
            y += u * K
            return x, y


C, R = map(int, input().split())
K = int(input())

if C * R >= K:
    print(*arrange_seat(C, R, K))
else:
    print(0)