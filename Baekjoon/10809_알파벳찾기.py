al = [-1] * 26
cnt = 0
word = input()
for w in word:
    al[ord(w)-97] = cnt
    cnt += 1
print(*al)