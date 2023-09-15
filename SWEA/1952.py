# 수영장

def calc_fee(n, fee):
    global ans
    if n >= 12:
        if ans > fee:
            print(fee)
        ans = min(ans, fee)
        return

    calc_fee(n+1, fee+day*plans[n])
    calc_fee(n+1, fee+one)
    calc_fee(n+3, fee+triple)

for tc in range(1, int(input())+1):
    day, one, triple, year = map(int, input().split())
    plans = [0]+list(map(int, input().split()))
    ans = year
    # dp = [0]*13

    # dp[1] = min(day*plans[1], one)
    # dp[2] = dp[1]+min(day*plans[2], one)
    # for i in range(3, 13):
    #     dp[i] = min(dp[i-3]+triple, dp[i-1]+min(one, day*plans[i]))

    calc_fee(0, 0)
    # print(f'#{tc}', min(dp[-1], year))
    # print(dp)