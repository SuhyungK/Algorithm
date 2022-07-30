# 176ms
# sys.stdin.readline()이 input()보다 확실히 빠르다
# 하나씩 입력받은 다음에 다시 출력하면서 거꾸로 출력
import sys

T = int(input())

for _ in range(T):
    S = sys.stdin.readline().split()
    for s in S:
        print(s[::-1] + ' ',end='')
    print()


# 처음풀이
# 776ms
T = int(input())

for _ in range(T):
    S = input().split()
    for s in S:
        print(s[::-1] + ' ',end='')
    print()
