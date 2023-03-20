# 공주님의 정원

import sys
input = sys.stdin.readline

N = int(input())

flw = [(100 * m1 + d1, 100 * m2 + d2) for m1, d1, m2, d2 in (map(int, input().split()) for _ in range(N))]
flw.sort()

# now : 마지막 꽃이 지는 날짜(3월 1일부터 시작)
# ans : 개수 
# max_end : 가장 마지막 꽃이 지는 날짜
now, ans, max_end = 301, 0, 0
for s, e in flw:
    if s == e: # 그 날 피어서 그 날 지는 경우 제외
        continue

    if s <= now: # 현재 비교하고 있는 꽃의 피는 날짜 < 마지막 꽃이 지는 날짜
        if now < e and max_end < e: # 마지막 꽃이 지는 날짜 < 현재 비교하고 있는 꽃의 지는 날짜 여야만 비교 가능
            max_end = e
        elif e <= now: # 마지막 꽃이 지는 날짜가 현재 비교하고 있는 꽃의 지는 날짜보다 크다면 비교할 이유 X
            continue
    else:
        if max_end < s: # 가장 늦게 지는 꽃의 날짜가 다음 비교해야 할 꽃의 피는 날짜보다 작다면 연결되지 않으므로 종료
            break
        else:
            """
            만약 현재 비교하고 있는 꽃의 피는 날짜가 현재로서 가장 마지막 꽃이 지는 날짜(now)보다 크다면
            연결은 되지만 다음 비교를 위해서는 now를 업데이트 해줘야 함
            """
            now, max_end = max_end, e
            ans += 1

    if e > 1130:
        ans += 1     
        break

print(ans if max_end > 1130 else 0)