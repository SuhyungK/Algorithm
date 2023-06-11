# View

for tc in range(10):
    view = 0
    n = int(input())
    arr = list(map(int, input().split()))
   
    for i in range(2, n-2):
        cnt = []
        for j in range(i-2,i):
            cnt.append(arr[j])
        for k in range(i+1,i+3):
            cnt.append(arr[k])
        for m in range(4):
            if arr[i] < cnt[m]:
                break
        else:
            view += (arr[i] - max(cnt))

    print(f'#{tc+1} {view}')

# 2
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

