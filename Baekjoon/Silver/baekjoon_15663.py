def comb(k):
    if k == M:
        print(*lst)
        return 
    
    prev = -1
    for i in range(N):
        if not check[i] and prev != arr[i]:
            lst[k] = arr[i]
            check[i] = True
            comb(k+1)
            prev = arr[i]
            check[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
check = [False]*N
lst = [-2]*M

comb(0)