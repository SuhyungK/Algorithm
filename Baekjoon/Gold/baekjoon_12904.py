# A와 B
# 거꾸로 해결하면 되는 문제! T -> S로 찾아서 내려오는 방법은 한 가지다

S = list(input())
L = list(input())

N = len(L) - len(S)
for _ in range(N):
    if L[-1] == 'A':
        L.pop()
    elif L[-1] == 'B':
        L.pop()
        L = L[::-1]
        
if L == S:
    print(1)
else:
    print(0)