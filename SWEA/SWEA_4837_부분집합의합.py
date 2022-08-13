arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for test_case in range(T):
    n, k = map(int, input().split())
    
    cnt = 0
    for i in range(1<<len(arr)):
        c = s = 0 #c : 원소의 개수 s: 부분집합의 합
        for j in range(len(arr)):
            if i & (1<<j):
                c += 1
                s += arr[j]
                if c > n: # n보다 크게 생성된 경우, 메모리 절약
                    break
        if c == n and s == k:
            cnt += 1

    if cnt:
        print(f'#{test_case+1} {cnt}')
    else:
        print(f'#{test_case+1} 0')