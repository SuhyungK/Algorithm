# 자릿수 더하기

N = input()

s = 0
for n in N:
    s += int(n)

print(s)



#처음 풀이
a = int(input())
m = 0
sum = 0
while a > 0:
  m = a % 10
  a = a // 10
  sum = sum + m

print(sum)