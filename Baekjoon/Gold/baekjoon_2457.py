# G3 공주님의 정원

"""
1. **꽃이 지는 날짜 기준**이 속할 수 있는 날짜 구간을 찾은 다음에 그 구간들 가운데서 가장 오랫동안 피어 있을 수 있는 구간을 찾는다
2. 그 구간의 꽃이 지는 날짜를 다음 **꽃이 지는 날짜 기준**으로 정한다
    
    2-1. 이렇게 정해질 때 꽃의 개수에 카운트 + 1 을 해주면 된다
    
    2-2. 꽃이 지는 날짜 기준이 속할 수 있는 날짜 구간을 찾지 못한 상태로 꽃이 피는 날짜가 11월 30일을 넘어선다면 꽃의 개수는 0으로 초기화하고 종료된다
    
3. 1, 2의 과정을 반복한다
4. 꽃이 지는 날짜 기준이 11월 30일을 넘어서게 된다면 종료한다
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
months = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = sum(months[:4]) + 1
e = sum(months) - 31
for m in range(2, 13):
    months[m] += months[m-1]

flw = [(months[m1] + d1, months[m2] + d2) for m1, d1, m2, d2 in (map(int, input().split()) for _ in range(N))]
flw.sort(key=lambda x: (x[0], -x[1]))

while s <= e:
    pass
