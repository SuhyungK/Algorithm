import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    minV = n*m
    for i in range(1, n-1):
        for j in range(i+1, n):
            cnt = 0
            for white in arr[:i]:
                for w in white:
                    if w != 'W':
                        cnt += 1
            for blue in arr[i:j]:
                for b in blue:
                    if b != 'B':
                        cnt += 1
            for red in arr[j:]:
                for r in red:
                    if r != 'R':
                        cnt += 1
            if minV > cnt:
                minV = cnt

    print(f'#{tc+1}', minV)