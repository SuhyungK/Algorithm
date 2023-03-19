# 거스름돈

n = int(input())

for m in range(n//5, -1, -1):
    cnt = m
    k = n - 5*m
    if not k%2:
        cnt += k//2
        break
else:
    cnt = -1
print(cnt)