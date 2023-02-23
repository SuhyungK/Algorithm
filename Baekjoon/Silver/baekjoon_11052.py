# S1 카드 구매하기

N = int(input())
card = [0] + list(map(int, input().split()))

for i in range(N+1):
    for j in range(i):
        card[i] = max(card[i-j] + card[j], card[i])

print(card[N])