from re import S
import sys
sys.stdin = open('SWEA_1209.txt')

def maxSum(s1, s2):
    return s1 if s2 < s1 else s2
        
for test_case in range(10):
    maxV = 0
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)] # 초기화
    
    # 행의 합, 열의 합
    for i in range(100):
        s1 = s2= 0 # 실질적으로 덧셈 해주는 반복문 위에 있어야
        for j in range(100):
            s1 += arr[i][j]
            s2 += arr[j][i]
        maxV = maxSum(maxV, maxSum(s1, s2))


    # 대각선의 합
    s1 = s2 = 0
    for i in range(100):
        s1 += arr[i][i]
        s2 += arr[i][99-i]
    maxV = maxSum(maxV, maxSum(s1, s2))


    print(f'#{test_case+1} {maxV}')
