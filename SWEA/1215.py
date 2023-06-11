# 회문 1

for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    re_arr = list(map(list, zip(*arr)))
    cnt = 0

    for idx in range(9-n):
        for row in arr:
            temp = row[idx:idx+n]
            if temp == temp[::-1]:
                cnt += 1

        for col in re_arr:
            temp_col = col[idx:idx+n]
            if temp_col == temp_col[::-1]:
                cnt += 1

    print(f'#{tc}', cnt)