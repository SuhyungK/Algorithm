N = int(input())

i = 1
while 1:
    if N <= 1:
        break
    N -= 6*i
    i += 1

print(i)