# 요세푸스 문제 

N, k = map(int, input().split())
arr = [i for i in range(1, N+1)]
lst = []

i = k-1
while 1:
    lst.append(arr.pop(i))
    if len(lst) == N:
        break
    # 원래 k칸만큼 이동이지만 현재 위치에 있던 값이 빠졌기 때문에 k-1칸만큼만 이동하면 됨
    # 길이가 계속해서 줄어들고 + 순환 큐처럼 돌아야 하기 때문에 
    i = (i+k-1)%len(arr)

print('<'+', '.join(map(str, lst)) +'>')