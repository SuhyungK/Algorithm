# ZOAC

string = input()
L = len(string)
ans = ['']*L

def search(i):
    global ans
    minOrd, idx = 150, -1
    for k in range(i, L):
        if ans[k] != '':
            return idx
        if ord(string[k]) < minOrd:
            minOrd = ord(string[k])
            idx = k
    return idx

def zoac(i):
    while True:
        idx = search(i+1)
        if idx == -1:
            return 
        ans[idx] = string[idx]
        print(''.join(ans))
        zoac(idx)
        
zoac(-1)