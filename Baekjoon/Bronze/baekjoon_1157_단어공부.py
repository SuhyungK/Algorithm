word = input().lower()
alpha = list(set(word))
cnt = [word.count(a) for a in alpha]

if (cnt.count(max(cnt))) >= 2: # 최대인 숫자가 유일한지 아닌지 판별
    print('?')
else:
    print(alpha[cnt.index(max(cnt))].upper())
    # alpha와 cnt는 각각의 알파벳과 개수 인덱스값이 동일선상에 있음