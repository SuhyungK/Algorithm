#나중 풀이
#문자열 그대로 입력받아서 더해줄때만 숫자로 변경

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