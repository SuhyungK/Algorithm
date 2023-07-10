def check(n):
    return str(bin(n)).count('1')

def solution(n):
    answer = 0
    
    # 2진수로 변환했을 때 1의 개수 
    one = check(n)
    
    next = n
    while True:
        next += 1
        if check(next) == one:
            return next