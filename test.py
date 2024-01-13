N = int(input())
lst = [i for i in range(1, N+1)]

t = 1
idx = 0
while len(lst) > 1:
    idx = (idx + (t * t * t) - 1) % len(lst)
    lst.pop(idx)
    t += 1

print(lst[0])