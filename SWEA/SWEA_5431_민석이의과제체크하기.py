# T = int(input())
# for tc in range(T):
#     n, k = map(int, input().split())
#     lst = sorted([0] + list(map(int, input().split())) + [n+1])
#
#     print(f'#{tc+1} ', end='')
#     for i in range(k+1):
#         for j in range(lst[i]+1, lst[i+1]):
#             print(j, end=' ')
#     print()

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = [i+1 for i in range(n)]
    for j in range(k):
        temp.remove(lst[j])

    print(f'#{tc+1}', *temp)