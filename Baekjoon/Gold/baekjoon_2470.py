# 두 용액

def sol():
    N = int(input())
    solution = list(map(int, input().split()))

    solution.sort()
    l, r = 0, N-1
    min_diff, min_sols = 1e13, []
    while l < r:
        tmp = solution[l] + solution[r]
        if abs(tmp) < min_diff:
            min_diff = abs(tmp)
            min_sols = [l, r]
        
        if tmp >= 0:
            r -= 1
        else:
            l += 1

    print(solution[min_sols[0]], solution[min_sols[1]])

if __name__ == '__main__':
    sol()