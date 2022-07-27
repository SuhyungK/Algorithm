# 연/월/일 유효성 검사

month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
 
for t in range(T):
    date = input()
    y = int(date[:4]) # 1~4 연도
    m = int(date[4:6]) # 5~6 월
    d = int(date[6:8]) # 7~8 일
    if 0 < m < 13 and 0 < d <= month_date[m - 1]: 
        print(f'#{t + 1} {y:04d}/{m:02d}/{d:02d}')
    else:
        print(f'#{t + 1} -1')