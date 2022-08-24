N = int(input())
star = "*" * N

for n in range(N):
    if n % 2:
        print(" " + " ".join(star))
    else:
        print(" ".join(star))


#어렵게 생각할 필요 없이 옆의 공백만 생각하면 되는 문제
for n in range(N):
    if n % 2:
        print(" *")
    else:
        print("* ")