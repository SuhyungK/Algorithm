def solution(n):
    ans = ""
    while n > 0:
        n, r = divmod(n, 3)
        if not r:
            n -= 1
            r = 4
        ans += str(r)
    return ans[::-1]