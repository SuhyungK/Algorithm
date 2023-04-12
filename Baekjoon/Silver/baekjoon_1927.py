# 최소 힙

def top():
    res.append(heap[1])

def insert(n):
    heap.append(n)
    c = len(heap) - 1
    p = c // 2
    while p >= 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def delete():
    heap[1], heap[-1] = heap[-1], heap[1]
    heap.pop()
    p = 1
    while (lc:=p*2) <= len(heap)-1:
        min_c = lc
        if (rc:=p*2+1) <= len(heap)-1 and heap[lc] > heap[rc]:
            min_c = rc
        if heap[min_c] > heap[p]: 
            break
        heap[min_c], heap[p] = heap[p], heap[min_c]
        p = min_c

N = int(input())
heap = [0]
res = []

for _ in range(N):
    ipt = int(input())
    if ipt == 0:
        if len(heap) == 1:
            res.append(0)
        else:
            top()
            delete()
    else:
        insert(ipt)

print('\n'.join(map(str, res)))