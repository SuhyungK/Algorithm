T = int(input())
 
for t in range(T):
    N = int(input())
 
    # 입력받는 문자열 하나의 문자열로 정리
    s = ""
    for n in range(N):
        alpha, num = input().split()
        s += alpha * int(num)
 
 
    # 슬라이싱 연산자 통해 10개 단위로 끊어서 출력
    print(f'#{t + 1}')
    for i in range(0, len(s), 10):
        print(s[i:i + 10])