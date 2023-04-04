# 달팽이는올라가고싶다

# 1
# 시간초과로 반복문 돌리면 실패하는 문제
# A : 올라가는 길이 B : 내려오는 길이 V : 최종길이
# 낮에 A만큼 올라가서 꼭대기를 넘어서게 되면 다시 B만큼 밤에 내려올 일이 없으므로 
# 항상 A가 B보다 하루 더 앞서게 된다. 둘다 같은 날(Day)만큼 오르고 내려오게 된다면 영원히 도달할 수 없다
# 이해 안 되면 그냥 그려
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
D = (V - B) / (A - B)

print(int(D) if D == int(D) else int(D)+1)


# 2
import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
D = (V - B) / (A - B)

print(math.ceil(D))
