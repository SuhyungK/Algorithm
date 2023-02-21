# BOJ G5 숫자고르기

N = int(input())
lst = list(int(input()) for _ in range(N))
v = [0] * (N+1)
ans = 0

def cycle(node, s):
    global ans
    for i in range(1, N+1):
        if node == s:
            ans += 1
            v[node] = 1
            return 
        node = lst[node-1]

for i in range(1, N+1):
    cycle(lst[i-1], i)

print(sum(v))
for i in range(1, N+1):
    if v[i]:
        print(i)