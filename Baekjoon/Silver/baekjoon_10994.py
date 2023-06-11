# 별 찍기 - 19

N = int(input())
arr = [[' ']*(4*N-3) for _ in range(4*N-3)]

def recur_star(n, k):
    if not n:
        return 
    
    for c in range(4*n-3):
        arr[k][k+c] = '*'
        arr[k+4*n-4][k+c] = '*'

    for r in range(k+1, k+4*n-4):
        arr[r][k] = '*'
        arr[r][-1-k] = '*'

    recur_star(n-1, k+2)

recur_star(N, 0)
for row in arr:
    print(''.join(row))