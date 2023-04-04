# 완전제곱수

# 1 코드는 좀 더 긴데 시간은 좀 더 짧음
m = int(input())
n = int(input())

s = 0
min = n
for k in range(m, n+1):
    if int(k**0.5)**2 == k:
        s += k
        if k < min:
            min = k
if not s:
    print(-1)
else:
    print(s)
    print(min)


# 리스트쓰면 내장함수 때문에 편하긴 한데 시간이 좀 더 걸림
m = int(input())
n = int(input())

ps = []
for k in range(m, n+1):
    if int(k**0.5)**2 == k:
        ps.append(k)

if not ps:
    print(-1)
else:
    print(f'{sum(ps)}\n{min(ps)}')