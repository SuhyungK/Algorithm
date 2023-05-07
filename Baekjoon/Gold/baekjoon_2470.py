# 두 용액

N = int(input())
properties = list(map(int, input().split()))
properties.sort()

for i in range(N):
    now = properties[i]
    left, right = i+1, N - 1
    min_sum = float('inf')
    while left <= right:
        m = (left + right) // 2
        if abs(now - properties[m]) >= min_sum:
            left = m + 1
        else:
            min_sum = abs(now - properties[m])
            right = m - 1
print(min_sum)

