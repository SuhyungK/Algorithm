# A

A = int(input())
X = int(input())

ans = 1
for i in bin(X)[2:][::-1]:
    if i == '1':
        ans *= A
        ans %= 1000000007
    A = (A ** 2) % 1000000007

print(ans)
    