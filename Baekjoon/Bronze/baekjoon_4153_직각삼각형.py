while 1:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    lst.sort()
    num = sum(map(lambda x :  int(x) ** 2, lst[:2]))
    if num == (lst[-1] ** 2):
        print('right')
    else:
        print('wrong')