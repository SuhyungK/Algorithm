n = int(input())
star = [[" "] * n for _ in range(n)]

def draw(n, x, y):
    if n == 1:
        star[x][y] = "*"
        return 
    
    for i in range(x, x+n, n//3):
        for j in range(y, y+n, n//3):
            if (i, j) == (x+n//3, y+n//3): continue
            draw(n//3, i, j)

draw(n, 0, 0)
for row in star:
    print("".join(row))