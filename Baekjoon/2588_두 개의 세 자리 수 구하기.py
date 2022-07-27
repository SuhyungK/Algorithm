# (세 자리 수) x (세 자리 수)
# 백의 자리, 십의 자리, 일의 자리 순서로 돌아가며 곱하기

n1 = int(input())
n2 = int(input())
result = 0

for i in range(3):
    rest = n1 * (n2 % 10)
    print(rest)
    result += rest * (10 ** i)
    n2 //= 10

print(result)

# 1 

n = int(input())
m = input()

for i in m[::-1]:
    print(n * int(i))
print(n * int(m))

# 2 

n = int(input())
m = input()

print(n * int(m[-1]))
print(n * int(m[-2]))
print(n * int(m[0]))
print(n * int(m))