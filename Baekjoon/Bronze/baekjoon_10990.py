# 별찍기 15

#별 두 개가 겹쳐서 나오는 문제 때문에
#왼쪽에 나오는 별 먼저 찍고
#오른쪽에 나오는 별 나중에 찍음
N = int(input())

for n in range(N):
    print(" " * (N - n - 1) + "*", end='')
    if n > 0:
        print(" " * (2 * n - 1) + "*",end='')
    print()


#첫 번째 줄만 따로 찍음
N = int(input())

print(" " * (N-1) + "*")
for n in range(1, N):
    print(" " * (N-n-1) + "*" + " " * (2*n-1) + "*")


#길이가 다르긴 한데 시간은 똑같;

#     *
#    * *
#   *   *
#  *     *
# *       *