# 피보나치 수 4

n = int(input())

k = 0
f1, f2 = 0, 1
while k < n:
    f1, f2 = f2, f1+f2
    k += 1
print(f1)