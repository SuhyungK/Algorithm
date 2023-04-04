# N과 M 8

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def sequence(idx, lst, level):
    if level == m:
        print(*lst)
        return

    for i in range(idx, n):
        sequence(i, lst+[arr[i]], level+1)

sequence(0, [], 0)
