# join 함수도 기억이 안났고
# sort랑 sorted 차이고 여전히 헷갈리고
# 중복은 set을 써야 한다는 것만 잘 기억한듯

import sys
input = sys.stdin.readline

N = int(input())
S = {input().strip() for _ in range(N)}
S = sorted(list(S))
S.sort(key=lambda x: len(x))
print('\n'.join(S))
