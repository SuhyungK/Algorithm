# 과제 안 내신 분..?

ans = {n for n in range(1, 31)}
enroll = {int(input()) for _ in range(28)}

print('\n'.join(map(str, sorted(list(ans-enroll)))))