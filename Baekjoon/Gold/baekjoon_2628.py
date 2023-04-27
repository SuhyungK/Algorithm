# 종이 자르기

h, v = map(int, input().split())
n = int(input())

row, col = [], []
for _ in range(n):
    check, num = map(int, input().split())
    if check == 0:
        row.append(num)
    else:
        col.append(num)

row = sorted([0] + row + [v])
col = sorted([0] + col + [h])

max_r = max_c = 0 
for r in range(1, len(row)):
    if (t:=row[r] - row[r-1]) > max_r:
        max_r = t

for c in range(1, len(col)):
    if (t:=col[c] - col[c-1]) > max_c:
        max_c = t

print(max_r * max_c)