def solution(s):
    x = s

    answer = [0, 0]
    while x != '1':
        c = 0
        for i in x:
            if int(i): c += 1

        answer[1] += len(x) - c
        answer[0] += 1

        x = str(bin(c)[2:])

    return answer