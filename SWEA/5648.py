# 원자 소멸 시뮬레이션

from heapq import heappop, heappush

def time_calc(x1, y1, d1, x2, y2, d2):

    if d1 == d2:
        return 0
    
    if d1 == 0:
        if d2 == 1 and y2>y1 and x1==x2:
            return (y2-y1)/2
        elif d2 == 2 and x2-x1==y2-y1>0:
            return x2-x1
        elif d2 == 3 and x1-x2==y2-y1>0:
            return x1-x2
    elif d1 == 1:
        if d2 == 0 and y1>y2 and x1==x2:
            return (y1-y2)/2
        elif d2 == 2 and y1-y2==x2-x1>0:
            return y1-y2
        elif d2 == 3 and y1-y2==x1-x2>0:
            return y1-y2
    elif d1 == 2:
        if d2 == 0 and x1-x2==y1-y2>0:
            return x1-x2
        elif d2 == 1 and x1-x2==y2-y1>0:
            return x1-x2
        elif d2 == 3 and x1>x2 and y1==y2:
            return (x1-x2)/2
    elif d1 == 3:
        if d2 == 0 and x2-x1==y1-y2>0:
            return x2-x1
        elif d2 == 1 and x2-x1==y2-y1>0:
            return x2-x1
        elif d2 == 2 and x2>x1 and y1==y2:
            return (x2-x1)/2

    return 0

for tc in range(int(input())):
    N, atom = int(input()), []
    for _ in range(N):
        atom.append(list(map(int, input().split())))
    
    pq = []
    for i in range(N-1):
        x1, y1, d1 = atom[i]
        for j in range(i, N):
            result = time_calc(x1, y1, d1, atom[j][:3])
            if result:
                heappush(pq, (result, i, j))
    
    exploded, total_energy = [False]*len(atom), 0
    while pq:
        exploded_time = pq[0][0]
        exploded_atoms = set()

        while pq and pq[0][0] == exploded_time:
            time, i, j = heappop(pq)

            if exploded[i] or exploded[j]:
                continue

            exploded_atoms.add(i)
            exploded_atoms.add(j)

        for k in exploded_atoms:
            exploded[k] = True
            total_energy += atom[k][3]

    print(f'#{tc+1} {total_energy}')