def solution(msg):
    result = []
    dic = {chr(64+i): i for i in range(1, 27)}
    
    idx, s = 27, ''
    msg = list(msg[::-1])
    while True:
        if s and not dic.get(s):
            result.append(dic[s[:-1]])
            dic[s], s = idx, s[-1]
            idx += 1
            continue
        if not msg:
            result.append(dic[s])
            return result
        s += msg.pop()