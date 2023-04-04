# 비즈마켓

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=1)
B = sorted(list(map(int, input().split())))

sumV = 0
i = j = 0
while i < N:
    sumV += A[i] - B[j]
    j += 1
    if j == M:
        break
    i += 1
    
print(sumV)