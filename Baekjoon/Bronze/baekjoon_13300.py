# 방 배정

N, K = map(int, input().split())

rooms = {}
for _ in range(N):
    stu = input()
    if rooms.get(stu):
        rooms[stu] += 1
    else:
        rooms[stu] = 1

cnt = 0
for room in rooms.values():
    if not room % K:
        cnt += room // K 
    else: 
        cnt += (room // K) + 1

print(cnt)