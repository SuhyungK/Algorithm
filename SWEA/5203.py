# 베이비진 게임

def babygin(lst):
    j = 0
    while j < 10:
        if lst[j] >= 3:
            return 1
        elif lst[j] >= 1 and lst[j+1] >= 1 and lst[j+2] >= 1:
            return 1
        j += 1
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    c1, c2, ans = [0]*12, [0]*12, 0

    for i in range(6):
        c1[arr[2*i]] += 1
        c2[arr[2*i+1]] += 1
        if babygin(c1):
            ans = 1
            break
        elif babygin(c2):
            ans = 2
            break

    print(f'#{tc}', ans)
