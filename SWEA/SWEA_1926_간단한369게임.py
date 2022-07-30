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

# 10
# 1 2 - 4 5 - 7 8 - 10