# 이중우선순위큐

def solution(operations):
    answer = [0, 0]
    digit = defaultdict(int)
    Q1, Q2 = [], [] # Q1은 최소큐, Q2는 최대큐
                
    for s in operations:
        op, n = s.split()
        n = int(n)
        if op == 'I':
            heappush(Q1, n)
            heappush(Q2, -n)
            digit[n] += 1
        elif n == 1:
            while Q2:
                if digit[-Q2[0]]:
                    digit[-heappop(Q2)] -= 1
                    break
                heappop(Q2)
        elif n == -1:
            while Q1:
                if digit[Q1[0]]:
                    digit[heappop(Q1)] -= 1
                    break
                heappop(Q1)
    
    sum_digit = sum(digit.values())
    if sum_digit == 0:
        return ['EMPTY']
    
    if sum_digit == 1:
        for k, v in digit.items():
            if v:
                return [k, k]
    
    # 최대 값 반환
    while Q2:
        if digit[-Q2[0]]:
            answer[0] = -heappop(Q2)
            break
        heappop(Q2)
    
    while Q1:
        if digit[Q1[0]]:
            answer[1] = heappop(Q1)
            break
        heappop(Q1)
    return answer

from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    operations = [input() for _ in range(int(input()))]
    print(*solution(operations))