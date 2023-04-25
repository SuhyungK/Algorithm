# 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 0, max(trees) - 1
while s+1 < e:
    m = (s+e)//2
    tmp_sum = 0
    for t in trees:
        tmp = (t-m)
        if tmp > 0:
            tmp_sum += tmp
            if tmp_sum >= M:
                break
    
    if tmp_sum >= M:
        s = m
    else:
        e = m 

print(s)