# 이진탐색

# 문제에 주어진 조건이 start, end 값을 다시 초기화할 때
# mid+1 이나 mid-1 로 하는게 아니라 mid 값으로 해야 한다는 게 있었다는걸 못 봐서 계속 에러가 남
def binary_find(end, page):
    start = 1
    cnt = 0
    while start <= end:
        mid = int((start+end)/2)
        cnt += 1
        if mid == page:
            return cnt
        elif mid < page:
            start = mid
        else:
            end = mid
    return cnt


T = int(input())
for test_case in range(1, T+1):
    r, a, b = map(int, input().split())
    A = binary_find(r, a)
    B = binary_find(r, b)

    print(f'#{test_case} ',end='')
    if A < B:
         print('A')
    elif A == B:
         print(0)
    else:
         print('B')