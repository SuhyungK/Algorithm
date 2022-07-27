# 간단한 경우
N = int(input())
 
li = [1]
for n in range(2, N + 1):
    if N % n == 0:
        li.append(n)
 
print(*li)

N = int(input())
 

# 복잡한 경우
li = []
for n in range(1, int(N ** 0.5 + 1)): # 모든 수는 어떤 수(실수)의 제곱이다 그 수를 기준으로 약수들은 짝을 짓게 된다
    if N % n == 0:
        li.append(n)
        li.append(N // n)
 
li.sort()
 
print(*li)