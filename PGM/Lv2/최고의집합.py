def solution(n, s):
    if not s // n:
        return [-1]
    
    ans = [s//n]*(n-s%n) + [s//n+1]*(s%n)
    return ans