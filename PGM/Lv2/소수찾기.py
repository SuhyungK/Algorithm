def solution(nums):
    # nums에서 중복되지 않는 조합 구하기
    perm = set()
    for r in range(1, len(nums)+1):
        perm |= set(map(int, map("".join, permutations(list(nums), r))))
    
    # 0, 1은 제외
    perm -= set(range(0, 2))
    
    # 2, 3, 5, 7... 의 배수들 제외하기
    for i in range(2, int(max(perm)**0.5)+1):
        perm -= set(range(i * 2, max(perm)+1, i))
    
    return len(list(perm))
from itertools import permutations