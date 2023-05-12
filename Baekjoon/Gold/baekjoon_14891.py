# 톱니바퀴

"""
gear_pols : 톱니바퀴 4개에 대한 정보가 담긴 딕셔너리
K : 회전하는 횟수
now_gear : 회전하는 기어의 번호
rotate_dir : 회전하는 방향
left_gear : 왼쪽 기어
right_gear : 오른쪽 기어
refs : 현재 각 톱니바퀴들에서 12시 방향을 가리키고 있는 바퀴들의 번호

가장 처음에 12시 방향에 위치한 바퀴를 0번으로 해서 시계방향으로 1씩 증가하게 번호를 부여한다
번호는 0~7까지 존재한다
"""
def rotating(ref, dir):
    next_ref = ref - dir
    if next_ref > 7:
        return 0
    elif next_ref < 0:
        return 7
    else:
        return next_ref

def solution(gear_pols):
    refs, ans = [0, 0, 0, 0, 0], 0
    for _ in range(int(input())):
        now_gear, rotate_dir = map(int, input().split())
        new_refs = refs[:]
        now_ref = refs[now_gear]
        new_refs[now_gear] = rotating(now_ref, rotate_dir)

        left_gear, left_rotate = now_gear - 1, rotate_dir
        while left_gear >= 1:
            left_ref, right_ref = refs[left_gear], refs[left_gear+1]
            if gear_pols[left_gear][(left_ref+2)%8] == gear_pols[left_gear+1][right_ref-2]:
                break
            left_rotate *= -1
            new_refs[left_gear] = rotating(left_ref, left_rotate)
            left_gear -= 1

        right_gear, right_rotate = now_gear + 1, rotate_dir
        while right_gear < 5:
            right_ref, left_ref = refs[right_gear], refs[right_gear-1]
            if gear_pols[right_gear][right_ref-2] == gear_pols[right_gear-1][(left_ref+2)%8]:
                break
            right_rotate *= -1
            new_refs[right_gear] = rotating(right_ref, right_rotate)
            right_gear += 1
        
        refs = new_refs[:]
        
    for i in range(4):
        if gear_pols[i+1][refs[i+1]] == '1':
            ans += 2 ** i

    return ans


# 톱니바퀴 4개에 대한 input 받기
gear_pols = {}
for i in range(1, 5):
    gear_pols[i] = list(input())

print(solution(gear_pols))
