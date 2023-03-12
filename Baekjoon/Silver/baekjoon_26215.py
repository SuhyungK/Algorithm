# S3 눈 치우기

N = int(input())
snow = list(map(int, input().split())) + [0]

snow.sort(reverse=1)
ans = 0
while snow[1] > 0:
    snow[0] -= 1
    snow[1] -= 1
    snow.sort(reverse=1)
    ans += 1

ans += snow[0]
print(-1 if ans > 1440 else ans)