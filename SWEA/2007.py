# 패턴 마디의 길이

T = int(input())
 
for t in range(T):
    s = input()
 
    for n in range(2, 30):
        if s[:n] == s[n:2*n]:
            print(f'#{t+1} {n}')
            break

# KOREAKOREAKOREAKOREAKOREAKOREA
# 5