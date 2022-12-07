def solution(word):
    dic = []
    for r in range(1, 6):
        dic.extend(list(map("".join, product(['A', 'E', 'I', 'O', 'U'], repeat=r))))
        
    dic.sort()
    return dic.index(word)+1
from itertools import product