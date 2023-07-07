def solution(n,a,b):
    a -= 1
    b -= 1

    num = 1
    while True:
        a //= 2
        b //= 2
        
        # a와 b가 경기에서 만나게 되면 횟수 출력
        if a == b:
            return num
        num += 1