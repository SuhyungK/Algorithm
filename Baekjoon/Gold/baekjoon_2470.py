import sys
sys.stdin = open('input.txt')

positive, negative = [], []

N = int(input())
lst = list(map(int, input().split()))

for a in lst:
    if a > 0:
        positive.append(a)
    elif a < 0:
        negative.append(a)

print(positive, negative)