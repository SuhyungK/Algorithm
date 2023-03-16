def solution(scores):
    sco_sum = defaultdict(list)
    stad, rank = sum(scores[0]), 0
    for score in sorted(scores, key=lambda x: -sum(x)):
        sco_sum[sum(score)].append(score)
    
    sums = list(sco_sum.keys())
    e = sums.index(stad)
    for i in range(e):
        for j in range(i+1, e):
            if sums[i] >= sums[j] + 2:
                for u in sco_sum[i]:
                    for v in range(len(sco_sum[j]), -1, -1):
                        t = sco_sum[j][v]
                        if u[0] > t[0] and u[1] > t[1]:
                            sco_sum[j].pop(v)
                    print(sco_sum)
    return rank

from collections import defaultdict