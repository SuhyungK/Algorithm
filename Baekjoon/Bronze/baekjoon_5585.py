# B2 거스름돈

coins = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
ans = 0
for coin in coins:
    ans += money // coin
    money %= coin
    print(ans, coin)
print(ans)