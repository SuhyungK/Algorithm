import sys
sys.stdin = open('SWEA_4843.txt')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = [0] * 1000
    temp = [0] * N

    # 카운팅정렬
    for i in range(N):
        cnt[data[i]-1] += 1

    for i in range(1000):
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1):
        cnt[data[i]-1] -= 1
        temp[cnt[data[i]-1]] = data[i]

    print('#%d ' %(test_case), end='')
    for i in range(5):
        print(f'{temp[-1-i]} {temp[i]} ', end='')
    print()