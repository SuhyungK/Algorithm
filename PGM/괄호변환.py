def valid(p):
    stk = []
    for s in p:
        if s == '(':
            stk.append(s)
        else:
            if not stk:
                return False
            elif stk[-1] == '(':
                stk.pop()
    if not stk:
        return True
    else: return False
                
def solution(p):
    if p == '':
        return p
    t = 0
    u = v = ''
    for i in range(len(p)-1):
        if p[i] == '(':
            t += 1
        else:
            t -= 1
        if not t:
            u = p[:i+1]
            v = p[i+1:]
            break
    else: 
        u = p
    
    if valid(u):
        return u + solution(v)
    else:
        new_u = ''
        for _u in u[1:-1]:
            if _u == '(':
                new_u += ')'
            else:
                new_u += '('

        return '(' + solution(v) + ')' + new_u
    
print(solution("(()())()"))
