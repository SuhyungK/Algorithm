def solution(brown, yellow):

	# (가로, 세로) 순서쌍이 타일의 수와 일치하는지 여부 
    def check(m, n):
        return 2*m + (n-2)*2 == brown
    
    total = brown + yellow
    for n in range(2, int(total**0.5)+1):
        if total%n == 0 and check(total//n, n):
            return total//n, n