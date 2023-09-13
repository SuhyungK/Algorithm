def solution(arr):
    answer = [0, 0]
    def square(x1, y1, d):
        if d == 1:
            answer[arr[x1][y1]] += 1
            return {arr[x1][y1]}
        
        d //= 2
        s1 = square(x1, y1, d)
        s2 = square(x1, y1+d, d)
        s3 = square(x1+d, y1, d)
        s4 = square(x1+d, y1+d, d)
        if len(s1) == 1 and s1 == s2 == s3 == s4:
            answer[list(s1)[0]] -= 3
            return s1
        return set()

    square(0,0,len(arr))
    return answer