# 트럭

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

def move():
    queue = [0] * w
    sumW = time = next = 0
    while True:
        time += 1
        sumW -= queue.pop(0)
        if next < n and sumW + (trc:=truck[next]) <= L:
            sumW += trc
            queue.append(trc)
            next += 1
        else:
            queue.append(0)
        # print(queue, sumW, next)

        if not sumW and next == n:
            return time

print(move())