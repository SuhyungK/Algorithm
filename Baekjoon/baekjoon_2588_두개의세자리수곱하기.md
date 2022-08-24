## [두 개의 세 자리 수 곱하기](https://www.acmicpc.net/problem/2588)


```python
n1 = int(input())
n2 = int(input())
result = 0

for i in range(3):
    rest = n1 * (n2 % 10)
    print(rest)
    result += rest * (10 ** i)
    n2 //= 10

print(result)
```
- 풀이
    세 자리 숫자를 백의 자리, 십의 자리, 일의 자리 순서로 분해해야 했는데 10으로 나눠서 나머지를 구하는 방식으로 일일이 구했었다



```python
# 1 

n = int(input())
m = input()

for i in m[::-1]:
    print(n * int(i))
print(n * int(m))
```


### 남의 풀이 1
- 하나씩 계산해야 하는 두번째 숫자를 숫자가 아닌 문자로 받아서 반복문으로 거꾸로 하나씩 추출해서 계산해줬다. 
- 1. 기본적으로 input()은 문자형으로 입력받는다는 것과 
- 2. 형태만 맞으면 str->int 형변환이 가능하다는 점을 이용해 계산할 때만 바꿔주면 된다는 것을 알게되었다.


```python
# 2 

n = int(input())
m = input()

print(n * int(m[-1]))
print(n * int(m[-2]))
print(n * int(m[0]))
print(n * int(m))
```


### 남의 풀이2
- tr[-1] 형태를 취하면 iterable 형태의 자료형들을 뒤에서부터 추출할 수 있다는 점을 이용해 아예 반복문 없이 값을 출력하는 방식이었다. 
- 마찬가지로 계산할 때만 정수형으로 바꿔줬다. 





## 후기
- 죄다 반복문으로 하는 게 파이썬이랑 안 맞는 거 같다
- 어떤 방식으로 풀어도 4줄짜리 반복문보다는 나아보임