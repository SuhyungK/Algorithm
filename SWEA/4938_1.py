# 이진탐색

def binary_find(left, right, page, cnt = 0):
    cnt += 1
    if left > right:
        return cnt 
    mid = (left + right) // 2
    if mid == page:
        return cnt
    elif mid < page:
        return binary_find(mid, right, page, cnt)
    else:
        return binary_find(left, mid, page, cnt)


T = int(input())
for test_case in range(1, T+1):
    r, a, b = map(int, input().split())
    A = binary_find(1, r, a)
    B = binary_find(1, r, b)

    print(f'#{test_case} ',end='')
    if A < B:
         print('A')
    elif A == B:
         print(0)
    else:
         print('B')
