# [약수 구하기](https://www.acmicpc.net/problem/2501)

- [간단한 N의 약수 구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq)

---

## 문제 풀이
- 모든 수는 반드시 어떤 수의 제곱
- 때문에 약수는 항상 그 수의 1/2 제곱값을 기준으로 나뉨
- 제곱값보다 낮은 값의 약수들을 먼저 구한 뒤 그 값으로 수를 나눠 얻은 수 또한 약수


### 간단한 수의 경우

```python
N = int(input())
 
li = [1]
for n in range(2, N + 1):
    if N % n == 0:
        li.append(n)
 
print(*li)
```
- 1부터 자기 자신까지의 모든 수에 대하여 나눠서 0이 되는 수는 약수



### 복잡한 수의 약수

```python
N, K = map(int, input().split())

li = []
for n in range(1, int(N ** 0.5 + 1)): 
    if N % n == 0:
        li.append(n)
        if not (N ** 0.5 == n): 
            li.append(N // n)

li.sort()
if K <= len(li):
    print(li[K - 1])
else:
    print(0)
```
- 제곱하면 그 수가 되는 수를 기준점으로 하여 여기까지만 약수를 먼저 구함
- 제곱하여 그 수가 되는 값은 이미 약수로 리스트에 추가된 값이기 때문에 중복이 되는 걸 배제하기 위해 제외
- 인덱스 값이 리스트의 범위를 벗어나는 경우를 구하기 위해 리스트의 길이값으로 비교