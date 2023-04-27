N = int(input())
all = list(map(int, input().split()))
M = int(input())
items = list(map(int, input().split()))

# 이분탐색을 하기 위해 가지고 있는 전체 부품을 오름차순 정렬
all.sort()

# n 을 찾기 위한 이분탐색 함수
def binary_search(n):
    s, e = 0, N-1

    # 왼쪽값 s와 오른쪽 값 e가 같을 때도 비교를 해야 가장 양 끝 값이 정답일때도 비교할 수 있음
    while s <= e:
        m = (s+e)//2
        # n 을 찾게 되면 'yes'를 리턴
        if all[m] == n:
            return 'yes'
        elif all[m] > n:
            e = m - 1
        else:
            s = m + 1

    # 마지막까지 값을 찾지 못하고 반복문이 종료되면 'no' 출력
    return 'no'

res = []
for item in items:
    res.append((binary_search(item)))

print(*res)