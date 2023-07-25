# 이름 궁합

dic = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = input()
B = input()

alpha = []
for i in range(len(A)):
    alpha.append(dic[ord(A[i])-65])
    alpha.append(dic[ord(B[i])-65])

while len(alpha) != 2:
    new_alpha = []
    for j in range(len(alpha)-1):
        new_alpha.append((alpha[j]+alpha[j+1])%10)
    alpha = new_alpha[:]

print(f'{alpha[0]}{alpha[1]}')