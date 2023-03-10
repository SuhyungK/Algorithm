# G3 공주님의 정원

N = int(input())
months = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for m in range(2, 12):
    months[m] += months[m-1]

flw = [(months[m1] + d1, months[m2] + d2) for m1, d1, m2, d2 in (map(int, input().split()) for _ in range(N))]
print(flw)