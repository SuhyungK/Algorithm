arr = [11, 7, 5, 3, 2]
T = int(input())
for t in range(1,T+1):
    
    num = []
    N = int(input())

    for a in arr:
        cnt = 0
        while N != 1:
            if N % a:
                break
            else:
                N //= a
                cnt += 1
                continue
        num.append(cnt)


    print(f'#{t} ',end='')
    print(*num[::-1])