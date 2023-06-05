# 기타 레슨

def binary_search():
    s, t = max(lecs), sum(lecs)

    while s<=t:
        mid = (s+t)//2

        tmp, m = mid, M
        for l in lecs:
            if tmp+l>mid:
                m = m-1
                if m<0:
                    s=mid+1
                    break
                tmp = 0
            tmp += l
        else:
            t = mid-1
        
    print(s)

if __name__ == '__main__':
    N, M = map(int, input().split())
    lecs = list(map(int, input().split()))

    binary_search()