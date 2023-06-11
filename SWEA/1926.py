# 간단한 369 게임

keywords = '369'
N = int(input())
 
for n in range(1,N+1):
    count = 0
    for keyword in keywords:
        if str(n).count(keyword) >= 1:
            count += str(n).count(keyword)
 
    if count >= 1:
        print('-' * count + ' ', end='')
    else:
        print(f'{n} ', end='')


# 새로운 풀이
# 근데 시간 더 오래 걸림
keyword = '369'
N = int(input())

for n in range(1,N+1):
    n = str(n)
    cnt = 0
    for k in keyword:
        if k in n:
            cnt += n.count(k)
    if cnt != 0:
        print('-' * cnt + ' ', end='')
    else:
        print(f'{n} ', end='')

# 10
# 1 2 - 4 5 - 7 8 - 10