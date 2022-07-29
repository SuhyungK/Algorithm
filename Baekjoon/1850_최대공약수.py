# 최대공약수 구하기 : 유클리드 호제법
# 두 숫자의 최대 공약수 * '1' 
# 두 숫자를 1로 바꿔서 넣는 바람에 메모리 에러남
# 입력받는 두 숫자의 크기를 고려할 필요 없음
# 입력받는 숫자는 자연수이기 때문에 0이 입력되지 않음


# 숫자 크기를 고려하지 않아도 됨
import sys
input = sys.stdin.readline

def gcd(M, m):
    if M % m:
        return gcd(m, M % m)
    else:
        return m 

a, b = map(int, input().split())
print('1' * gcd(a, b))



# 처음 입력이 0일 수 없기 때문에 
# 아예 처음부터 나머지 값 m이 0이 되면 
# 최대공약수는 M 이라는 조건 식 설정

# def gcd(M, m):
#     if m == 0:
#         return M 
#     else:
#         return gcd(m, M%m)


# 처음 풀이
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