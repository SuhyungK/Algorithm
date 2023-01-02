# BOJ S4 A

A = int(input())
X = int(input())
l = len(str(bin(X)[2:]))
lst = [1] * l

lst[0] = A
for i in range(1, l):
    lst[i] = lst[i-1] ** 2

res = 1
for i in range(len(t:=str(bin(X)[2:][::-1]))):
    if t[i] == '1':
        res *= lst[i]

print(res % 1000000007)