# 풀이3
# datetime 이용
# 코드는 짧은데 시간 자체는 아래 둘 보다 오래 걸림
import datetime
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())
day = weekday[datetime.date(2007, x, y).weekday()]
print(day)



# 풀이1
# 월별 날짜를 일일이 반복문 돌려서 비교
x, y = map(int, input().split())
weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']
date = 0

for month in range(1, x):
    if month == 2:
        date += 28
    elif month  == 4 or month  == 6 or month == 9 or month == 11:
        date += 30
    else:
        date += 31
date += y
print(weekday[date % 7])


# 풀이2
# 월별 날짜를 아예 month 리스트로 만들고 가져다 씀
# 지나온 모든 날의 수를 더한 뒤 7일(일주일)로 나눠서 weekday 인덱스 값 구하기
weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = 0

x, y = map(int, input().split())
for m in range(x - 1):
    date += month[m]
date += y
print(weekday[date % 7])
