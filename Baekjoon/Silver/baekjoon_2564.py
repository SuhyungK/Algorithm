# BOJ 경비원

H, V = map(int, input().split()) # H : 가로 / V : 세로
stores = [tuple(map(int, input().split())) for _ in range(int(input()))]
dong = tuple(map(int, input().split())) # 동근이의 위치

# 1방향과 2방향에 놓인 걸 구하는거나 2방향과 1방향에 놓인 걸 구하는 건 같으니까
exp = {
    (1, 2): (lambda x: min(x[0] + x[1], 2*H - (x[0] + x[1])) + V), 
    (1, 3): (lambda x: x[0] + x[1]), 
    (1, 4): (lambda x: H - x[0] + x[1]), 
    (2, 3): (lambda x: x[0] + (V - x[1])), 
    (2, 4): (lambda x: (H - x[0]) + (V - x[1])), 
    (3, 4): (lambda x: min(x[0] + x[1], 2*V - (x[0] + x[1])) + H), 
}

d = 0
for store in stores:
    # 같은 방향에 있으면 걍 거리만 구하면 됨
    if dong[0] == store[0]: 
        d += abs(dong[1] - store[1])

    # 같은 방향에 놓여있지 않으면 각각 구해야함
    else:
        (p1, d1), (p2, d2) = sorted((store, dong))
        d += exp[(p1, p2)]((d1, d2))
    
print(d)