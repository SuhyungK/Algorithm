# 참외밭

n = int(input())
width, height = [], []

for _ in range(6):
    d, m = map(int, input().split())
    if d in (3, 4):
        height.append(m)
    else:
        width.append(m)

res = (max(height) * max(width) - height[1] * width[1]) * n
print(res)