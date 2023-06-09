# 소가 길을 건너간 이유 1

cow, ans = {}, 0

for _ in range(int(input())):
    num, bit = input().split()

    if not cow.get(num):
        cow[num] = bit
    
    elif cow[num] == bit:
        continue

    else:
        cow[num] = bit
        ans += 1

print(ans)