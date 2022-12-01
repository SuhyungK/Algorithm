for _ in range(int(input())):
    strn = input()
    res = 'YES'

    while strn:
        if strn[:2] == '01':
            strn = strn[2:]
        elif strn[:3] == '100':
            pass
            # 1. 0을 다 지우고 2가지로 나눠서 검사
            # 2. 뒤에 아무것도 없으면 걍 끝
            # 3. 뒤에 01로 시작하면 1다 지우기
            # 4. 뒤가 00
        else:
            res = 'NO'

    print(res)