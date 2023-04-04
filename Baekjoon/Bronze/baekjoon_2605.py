# 줄 세기

N = int(input())
lst = list(map(int, input().split()))
num = [1]

for idx, l in enumerate(lst[1:]):
    num.insert(l, idx+2)

print(*num[::-1])