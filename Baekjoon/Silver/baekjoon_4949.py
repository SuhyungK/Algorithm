# 균형 잡힌 세상

import sys
input = sys.stdin.readline

bracket = {')' : '(', '}' : '{', ']' : '['}
while 1:  
    string = input().rstrip()
    stack, ans = [], ''

    if string == '.':
        break
    else:
        for s in string[:-1]:
            if s.isalpha() or s == ' ': continue
            elif s in bracket.values():
                stack.append(s)
            elif s in bracket:
                if stack[-1:] == [bracket[s]]:
                    stack.pop()
                else:
                    ans = 'no'
            if ans:
                break
        else:
            ans = 'yes'
    
    if stack: ans = 'no'
    print(ans)