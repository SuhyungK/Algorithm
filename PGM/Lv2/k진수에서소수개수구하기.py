# 소수 판별 함수
def check(num):
    num = int(num)
    if num == 1:
        return 0
    
    for x in range(2, int(num**0.5)+1):
        if not num%x:
            return 0

    return 1

def solution(n, k):
    answer = 0
    
    # k진수로 변경
    new = []
    while n:
        n, v = divmod(n, k)
        new.append(v)
    
    new = new[::-1]
    
    # 소수가 될 숫자들 찾아내기
    new = ''.join(map(str, new)).replace('0',' ').split()
    
    # 소수인지 확인하기
    for num in new:
        answer += check(num)
        
    return answer