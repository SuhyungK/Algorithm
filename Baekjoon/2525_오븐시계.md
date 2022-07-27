#  [오븐 시계](https://www.acmicpc.net/problem/2525)

- 시간 추가 문제
- 60분을 넘으면 1시간 추가, 자정(24시)은 0시가 되는 점에 유의


## 풀이
```python
hr, min = map(int, input().split())
work = int(input())

_hr = work // 60
_min = work - _hr * 60 

min += _min
if min >= 60:
    min -= 60
    hr += 1
hr += _hr
if hr >= 24:
    hr -= 24

print(hr, min)
```
- 굳이 안 넣어줘도 될 시간 추가 변수(_hr, _min)를 선언
- 추가되는 시간(ex. 80분)을 60으로 나눴을 때 몫이 시간, 나머지가 시간이라는 점을 생각못함(_min 변수 부분)




## 다른 풀이

```python
hr, min = map(int, input().split())
work = int(input())

min += work % 60 # 추가된 분(minute)
hr += (work // 60 +  min // 60) # 추가된 시(hour) + 60분을 넘어 추가된 시간

min %= 60
hr %= 24

print(hr, min)
```
- 필요 없는 변수 없앰
- if 조건문 쓰지 않고 24시간 시스템이 24로 나눴을 때의 나머지값으로 돌아간다는 점 이용



```python
hr, min = map(int, input().split())
work = int(input())

_ = hr * 60 + min + work # 총 일한 분(minute)
hr = _ // 60 % 24 # 총 일한 시간 + 24시를 넘어갔을 때 자동 초기화
min = _ % 60 # 시간을 제외한 나머지 = minute, 몫으로 구함

print(hr, min)
```
- 시간 * 60 + 분을 통해서 전체적인 분(minute)을 구한다음에 60으로 각각 시각과 분을 구하는 방법
- 확실히 간단하긴 하다 너무 다 억지로 한줄에 쓰려고 하지 않고 한줄씩 쓴다면
- 변수 이름 짓기 귀찮아서 자꾸 _ 돌려쓰는 중...



## 후기
- 모든 변수를 60을 기준으로 접근해야한다고 생각하니까 너무 어렵게 생각함
- 무조건 파이썬이니까 간단하게 써야할 것 같다고 생각해서 반복문을 안 쓰려다보니까 어렵게 생각됨
- 짧은 코드들을 여러개 봤는데 가독성이 엉망같음, 
- 짧게 쓰기보다는 반복문 + 주석으로 알아보기 쉽게 짜는 게 더 나을 것 같다