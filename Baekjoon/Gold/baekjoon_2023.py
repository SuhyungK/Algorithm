#G5 신기한 소수

"""
2, 3, 5, 7 -> 23, 29, 31, 37 ... -> 233, ... 이런식으로 찾아나가기~
ans = {숫자의 길이: [그 숫자의 길이에 해당하는 숫자들 리스트]}
마지막에 ans[N] 출력하면 끝!
is_decimal 에서 어차피 뒤에 2가 붙는 건 소수 아니니까 2칸씩 뛰어 넘어서 계산
위에서 짝수 빼고 돌렸으니까 2, 4, 6, 8 같은 숫자로 나눠볼 필요 없으니까 여기도 2칸씩 넘어서 계산
근데 이러면 시간 줄어들 줄 알았는데 별로 의미없나바
"""

import math
N = int(input())
ans = {1: [2, 3, 5, 7]}

def is_decimal(num):
    for j in range(1, 10, 2):
        tmp = int(str(num) + str(j))
        for n in range(3, int(math.sqrt(tmp)) + 1, 2):
            if not tmp % n:
                break
        else: lst.append(tmp)

l = 1
while l < N:
    lst = []
    for a in ans[l]:
        is_decimal(a)
    l += 1
    ans[l] = lst

print('\n'.join(map(str, ans[l])))