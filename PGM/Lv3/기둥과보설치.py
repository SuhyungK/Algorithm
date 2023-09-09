def solution(n, build_frame):
    
    def possible(x, y, a):
        if a == 0: # 기둥일 때
            if y == 0: # 바닥일 때 
                return True
            if x>0 and arr[y][x-1][1]: # 왼쪽 아래에 보가 설치되어 있을 때
                return True
            if y<n and arr[y][x][1]: # 아래에 보가 설치되어 있을 때
                return True
            if y>0 and arr[y-1][x][0]: # 아래에 기둥이 있을 때
                return True
        else: # 보 일 때
            if y>0 and arr[y-1][x][0]: # 아래에 기둥이 있을 때
                return True
            if y>0 and x<n and arr[y-1][x+1][0]: # 아래 오른쪽에 기둥이 있을 때
                return True
            if x>0 and x<n and arr[y][x-1][1] and arr[y][x+1][1]: # 양 옆에 보가 다 존재할 때
                return True
        return False

    def remove_item(x, y, a):
        arr[y][x][a] = 0
        
        if a == 0: # 기둥일 때
            if y<n and arr[y+1][x][0] and not possible(x, y+1, 0): # 위에 기둥이 있는데 얘 없으면 안 될 때
                return False
            if y<n and arr[y+1][x][1] and not possible(x, y+1, 1): # 내 위에 보가 있는데 나 없인 안 될 때
                return False
            if y<n and x>0 and arr[y+1][x-1][1] and not possible(x-1, y+1, 1): # 왼쪽 위에 보가 있는데 얘 없으면 안 될 때
                return False
        else:
            if arr[y][x][0] and not possible(x, y, 0):
                return False
            if x<n and arr[y][x+1][0] and not possible(x+1, y, 0):
                return False
            if x>0 and arr[y][x-1][1] and not possible(x-1, y, 1):
                return False
            if x<n and arr[y][x+1][1] and not possible(x+1, y, 1):
                return False
        return True
    
    arr = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 0:
            if not remove_item(x, y, a):
                arr[y][x][a] = 1    
        else:
            if possible(x, y, a):
                arr[y][x][a] = 1
    
    result = []
    for y in range(n+1):
        for x in range(n+1):
            if arr[y][x][0]:
                result.append([x, y, 0])
            if arr[y][x][1]:
                result.append([x, y, 1])
    
    result.sort()
    return result