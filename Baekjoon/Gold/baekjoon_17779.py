# 게리맨더링 2

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(row) for row in arr])
ans = 1e9

# 1구역 구하기
def findOne(x, y, d1):
    one = 0
    for row in arr[:x]:
        one += sum(row[:y+1])
    
    for i in range(d1):
        one += sum(arr[x+i][:y-i])
    
    return one

# 2구역 구하기
def findTwo(x, y, d2):
    two = 0
    for row in arr[:x+1]:
        two += sum(row[y+1:])
    
    for i in range(1, d2+1):
        two += sum(arr[x+i][y+i+1:])

    return two

# 3구역 구하기
def findThree(x, y, d1, d2):
    three = 0
    for i in range(d2+1):
        three += sum(arr[x+d1+i][:y-d1+i])

    for row in arr[x+d1+d2+1:]:
        three += sum(row[:y-d1+d2])

    return three

# 4구역 구하기
def findFour(x, y, d1, d2):
    four = 0

    for i in range(1, d1+1):
        four += sum(arr[x+d2+i][y+d2-i+1:])

    for row in arr[x+d1+d2+1:]:
        four += sum(row[y-d1+d2:])
    
    return four

# 1~5구역 인구수 구해서 리스트로 만들고 최대 - 최소 값 반환하기
def Ward(x, y, d1, d2):
    ward = [findOne(x, y, d1), findTwo(x, y, d2), findThree(x, y, d1, d2), findFour(x, y, d1, d2)]
    ward.append(total-sum(ward))
    # print(x, y, d1, d2, ward)
    return max(ward)-min(ward)

for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x+d1+d2>=N or y-d1<0 or y+d2>=N:
                    continue
                print(x, y, d1, d2)
                t = Ward(x, y, d1, d2)
                if ans > t:
                    ans = t

print(ans)