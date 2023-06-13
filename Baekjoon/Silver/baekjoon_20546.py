# 기적의 매매법

cash = int(input())
stock = list(map(int, input().split()))


def jStock():
    global cash
    J = [cash, 0]
    for s in stock:
        cnt = J[0] // s
        if cnt: 
            J[0] -= cnt*s 
            J[1] += cnt
    return J[0]+J[1]*stock[-1]


def sStock():
    global cash
    S = [cash, 0]

    for i in range(3, 13):
        s = stock[i]
        if stock[i-3] < stock[i-2] < stock[i-1]:
            S[0] += S[1] * s
            S[1] = 0
        elif stock[i-3] > stock[i-2] > stock[i-1]:
            cnt = S[0] // s
            if cnt:
                S[0] -= cnt*s 
                S[1] += cnt
    return S[0]+S[1]*stock[-1]

jj = jStock(); ss = sStock()
if jj > ss:
    print('BNP')
elif jj == ss:
    print('SAMESAME')
else: 
    print('TIMING')