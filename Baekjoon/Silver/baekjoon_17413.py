# 단어 뒤집기 2
from collections import deque

string = list(input())

"""
1. 일반 문자열 : < 태그가 시작되거나 공백이 있으면 종료한다. 그 외의 문자는 반대로 뒤집는다
2. 태그 문자열 : < 로 시작하여 > 가 나오면 종료된다. 문자열을 뒤집지 않는다. 
"""

def reverse():
    global stack, ans
    while stack:
        ans += stack.pop()


stack, L = deque(), len(string)
idx, ans = -1, ''
while idx+1 < L:
    idx += 1
    word = string[idx]
    if word not in (' ', '<'):
        stack.append(word)
    else:
        reverse()
        if word == ' ':
            ans += ' '
            continue
        j = idx
        while j < L:
            stack.insert(0, string[j])
            if string[j] == '>':
                idx = j
                break
            j += 1
        reverse()
        
reverse()
print(ans)