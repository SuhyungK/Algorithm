# 수영장

import sys
sys.stdin = open('input.txt')

def calc_fee(n, fee):
    global ans
    # print(n, fee)
    if n >= 12:
        ans = min(ans, fee)
        return

    calc_fee(n+1, fee+day*plans[n])
    calc_fee(n+1, fee+one)
    calc_fee(n+3, fee+triple)    

for tc in range(1, int(input())+1):
    day, one, triple, year = map(int, input().split())
    plans = list(map(int, input().split()))
    ans = year

    calc_fee(0, 0)

    print(f'#{tc}', ans)