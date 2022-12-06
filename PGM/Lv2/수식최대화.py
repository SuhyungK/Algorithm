def solution(expression):
    expression = list(expression)
    
    nums, exp, char = [], [], ''
    while expression:
        tmp = expression.pop(0)
        if tmp in ('-', '*', '+'):
            nums.append(int(char))
            exp.append(tmp)
            char = ''
        else:
            char += tmp
    nums.append(int(char))
    
    def calc(a, b, e):
        if e == '-':
            return a-b
        elif e == '*':
            return a *b
        elif e == '+':
            return a+b
        
    def math(perm, nums, exp):
        for e in perm:
            nums.append(nums.pop(0))
            for _ in range(len(exp)):
                i = exp.pop(0)
                if i == e:
                    nums.append(calc(nums.pop(), nums.pop(0), e))
                else:
                    nums.append(nums.pop(0))
                    exp.append(i)
        return abs(*nums)
        
    ans = 0
    for perm in permutations(set(exp), len(set(exp))):
        ans = max(ans, math(perm, nums[:], exp[:]))
            
    return ans

from itertools import permutations