
def sol():
    left, right = 1, house[-1]-house[0]
    while left<=right:
        mid = (left+right)//2
        
        now, c = house[0], 1
        for next in house[1:]:
            if next>=now+mid:
                c += 1
                if c >= C:
                    break
                now = next

        if c >= C:
            left = mid+1
        else:
            right = mid-1

    print(right)

if __name__ == '__main__':
    sol()