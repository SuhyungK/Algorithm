# 회문2

def pali():
    for length in range(100, 1, -1):
        for row, col in zip(arr, re_arr):
            for idx in range(100 - length + 1):
                r = row[idx:idx+length]
                c = col[idx:idx+length]
                for i in range(length//2):
                    if r[i] != r[-1-i]:
                        break
                else:
                    return length

                for j in range(length//2):
                    if c[j] != c[-1-j]:
                        break
                else:
                    return length
    return 1

for _ in range(10):
    tc = input()
    arr = [list(input()) for _ in range(100)]
    re_arr = list(zip(*arr))

    print(f'#{tc}', pali())

