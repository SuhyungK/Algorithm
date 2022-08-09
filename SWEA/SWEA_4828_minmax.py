T = int(input())
for test_case in range(1, T + 1):
    cnt = int(input())
    arr = list(map(int, input().split()))
    max = min = arr[0]

    # max
    for M in range(cnt):
        max = arr[M] if max < arr[M] else max
    # min
    for m in range(cnt):
        min = arr[m] if min > arr[m] else min

    print(f'#{test_case} {max-min}')