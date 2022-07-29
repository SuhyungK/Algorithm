# 최대공약수 구하기 : 유클리드 호제법
# 두 숫자의 최대 공약수 * '1' 
# 두 숫자를 1로 바꿔서 넣는 바람에 메모리 에러남


import sys
input = sys.stdin.readline

def gcd(M, m):
    if M % m:
        return gcd(m, M % m)
    else:
        return m 

a, b = map(int, input().split())
print('1' * gcd(max(a, b), min(a, b)))

# 500000000000000000 500000000000000002
# 11 