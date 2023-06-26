N = int(input())
ans = [0] * N
for i in range(N):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        ans[i] = 10000 + 1000 * a
    elif a == b:
        ans[i] = 1000 + 100 * a
    elif b == c:
        ans[i] = 1000 + 100 * b
    elif c == a:
        ans[i] = 1000 + 100 * c
    else:
        ans[i] = max(a, b, c)

print(max(5, 6, 7))
print(max(ans))
       