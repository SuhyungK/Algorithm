for tc in range(10):
    view = 0
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(2, n-2):
        cnt = []
        min = 255

        for j in range(5):
            if j != 2:
                min = arr[i] - arr[i-2+j] if arr[i] - arr[i-2+j] < min else min
        
        if min > 0:
            view += min

    print(f'#{tc+1} {view}')

