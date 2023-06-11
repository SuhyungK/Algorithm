# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort()

    # 풀이 1
    print('#%d ' % tc, end='')
    for i, p in enumerate(person):
        if p // m * k - i <= 0:
            print('Impossible')
            break
    else:
        print('Possible')

    # 풀이 2 - 인덱스 접근 : 시간 더 짧음
    res = 'Possible'
    for i in range(n):
        ppang = person[i] // m * k - i
        if ppang <= 0:
            res = 'Impossible'
            break

    print(f'#{tc} {res}')