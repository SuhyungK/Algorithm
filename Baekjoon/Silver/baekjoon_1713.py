# BOJ S1 후보 추천하기
from collections import defaultdict

N = int(input())
R = int(input())
lst = list(map(int, input().split()))
res = defaultdict(int)

res[lst[0]] = 1
for i in range(1, R):
    if len(res) >= N:
        if lst[i] in res.keys():
            res[lst[i]] += 1
        else:
            mV, tmp = 1e9, 0 
            for k, v in res.items():
                if mV > v:
                    mV, tmp = v, k
            res.pop(tmp)
            res[lst[i]] = 1
    else:
        res[lst[i]] += 1

print(*sorted(res.keys()))