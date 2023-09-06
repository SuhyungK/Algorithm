def rotate(arr):
    return list(map(list, zip(*arr[::-1])))

def solution(key, lock):
    m, n = len(key), len(lock)
    hole = sum(n-sum(row) for row in lock)
    
    # 자물쇠에 처음부터 빈 홈이 없는 경우
    if not hole:
        return True
    
    # 열쇠를 4번 회전한 값 미리 저장
    rotate_arr = [key]
    for i in range(3):
        rotate_arr.append(rotate(rotate_arr[i]))
    
    # 열쇠가 자물쇠의 모든 홈을 채울 수 있는지 확인
    def match(i, j, key, hole):
        for ki in range(m):
            for kj in range(m):
                li, lj = i+ki, j+kj
                if not (-1<li<n and -1<lj<n):
                    continue
                
                # 열쇠와 자물쇠의 돌기가 겹치는 경우
                if key[ki][kj] and lock[li][lj]:
                    return False
                
                # 열쇠가 자물쇠의 홈을 채울 수 있는 경우
                if key[ki][kj] and not lock[li][lj]:
                    hole -= 1
        return not hole
    
    for i in range(-m+1, n):
        for j in range(-m+1, n):
            for k in range(4):
                if match(i, j, rotate_arr[k], hole):
                    return True
    return False