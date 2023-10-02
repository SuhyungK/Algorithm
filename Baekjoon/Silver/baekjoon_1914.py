# 하노이 탑

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, end, mid)
    print(start, end)
    hanoi(n-1, mid, start, end)

N = int(input())
turn, cnt = [], 0
print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)
