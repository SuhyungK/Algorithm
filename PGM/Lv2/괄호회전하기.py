pair = {'}': '{', ')': '(', ']': '['}

def check(_s):
    stack = [_s[0]]
    for strs in _s[1:]:
        if strs in ('{', '(', '['):
            stack.append(strs)
            continue

        if stack and stack.pop() != pair[strs]:
            return 0

    if stack:
        return 0
    return 1

def solution(s):
    if len(s) == 1:
        return 0

    ans = 0
    for i in range(len(s)):
        ans += check(s[i:]+s[:i])
    return ans