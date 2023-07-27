def solution(clothes):
    dic = {}
    for name, costume in clothes:
        dic[costume] = dic.get(costume, 1)+1
    
    answer = 1
    for v in dic.values():
        answer *= v
    return answer - 1