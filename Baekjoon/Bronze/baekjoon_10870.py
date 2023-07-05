# 피보나치 수  

def sol(n):
    if n == 0 or n == 1:
        return n
    n1, n2 = 0, 1
    i = 2
    while i<=n:
        n1, n2 = n2, n1+n2
        i += 1
    return n2
n = int(input())
print(sol(n))