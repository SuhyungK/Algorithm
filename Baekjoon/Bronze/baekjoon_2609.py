# 최대공약수

# 최소공배수 = (두 수의 곱) / (최대공약수)
# 최대공약수를 먼저 구하고 두 수를 곱한 뒤 나눠줌


def gcd(M, m):
    if m == 0:
        return M
    else:
        return gcd(m, M % m)

a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a * b // g)



# 처음 풀이
# 굳이 최소공배수 함수를 쓰는 게 비효율적
def gcd(M, m):
    if M % m:
        return gcd(m, M % m)
    else:
        return m 

def lcm(M, m):
    return M * m // gcd(M, m)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))