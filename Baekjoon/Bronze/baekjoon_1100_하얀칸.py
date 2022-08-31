res = [input() for _ in range(8)]

cnt = 0
for i in range(4):
    for j in range(4):
        if res[i*2][j*2] == 'F':
            cnt += 1
        if res[i*2+1][j*2+1] == 'F':
            cnt += 1

print(cnt)