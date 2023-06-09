# 오리

sound = input()
quack = [0, 0, 0, 0, 0]
quack_index = {
    'u': (0, 1), 'a': (1, 2), 'c': (2, 3), 'k': (3, 4)
}
def sol():
    for s in sound:
        if s == 'q':
            if quack[-1]>0: quack[-1] -= 1
            quack[0] += 1
        else:
            f, b = quack_index[s]
            if quack[f]>0: 
                quack[f] -= 1
                quack[b] += 1
            else:
                return -1

    if quack[-1] > 0:
        return quack[-1]
    return -1

print(sol())
