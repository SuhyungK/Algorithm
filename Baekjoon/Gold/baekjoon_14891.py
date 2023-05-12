# 톱니바퀴

gear = {}
for i in range(4):
    gear[i] = list(map(int, input()))

K = int(input())
rotate = [tuple(map(int, input().split())) for _ in range(K)]

def rotating(gear, rotate):
    for now_gear, rotate_dir in rotate:
        left_index = now_gear - 1
        while 0 <= left_index:
            if gear[left_index][2] == gear[now_gear][6]:
                break
            gear[left_index]
            left_index -= 1
            