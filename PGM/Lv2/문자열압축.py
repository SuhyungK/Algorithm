def solution(s):
    min_length = len(s) # 현재 최소 길이
    
    for i in range(1, len(s)+1):
        char, cnt, j, ps = s[:i], 1, i, ''
        while j < len(s):
            if s[j:j+i] != char:
                if cnt == 1:
                    ps += char
                else: 
                    ps += f"{cnt}{char}"
                char, cnt = s[j:j+i], 0
            cnt += 1
            j += i
        
        ps += char if cnt == 1 else f"{cnt}{char}"
        if len(ps) < min_length:
            min_length = len(ps)
            
    return min_length