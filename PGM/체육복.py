"""
lst : n명 학생들에 대한 체육복 정보가 담긴 리스트
각 칸에 담긴 개수만큼 체육복 소유
2 - 여벌옷, 1 - 1개뿐, 0 - 없음
최종적으로 전체에서 0개를 제외하면 체육복을 갖고 있을 수 있는 학생 수가 나옴

1) 앞에 있는 학생을 먼저 확인하는 경우
2) 뒤에 있는 학생을 먼저 확인하는 경우
두 가지로 나누어서 계산한 후에 더 큰 값을 답으로 
"""
def solution(n, lost, reserve):
    lst = [1] * (n+2)
    for l in lost:
        lst[l] = 0
    for r in reserve:
        lst[r] += 1
    
    lst2 = lst[:]
    c1 = 0
    for i in range(1, n):
        if lst[i] == 2:
            if lst[i-1] == 0:
                lst[i-1] = 1
            elif lst[i+1] == 0:
                lst[i+1] = 1

    for i in range(n, 0, -1):
        if lst2[i] == 2:
            if lst2[i-1] == 0:
                lst2[i-1] = 1
            elif lst2[i+1] == 0:
                lst2[i+1] = 1
                
    return n - min(lst.count(0), lst2.count(0))