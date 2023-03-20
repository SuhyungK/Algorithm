# 뱀과 사다리 게임

N, M = map(int, input().split())
ladder = {int(k) : int(v) for k, v in (input().split() for _ in range(N+M))}

"""
문제에서 시키는대로 잘 구현하자...
1. 어떤 위치든 일단 주사위를 던진다(1~6까지)
2-1. 그 던진 위치에 사다리나 뱀이 있으면 이동한다
2-2. 없다면 그 위치 그대로
3. 이제 이동했든 제자리든 그 위치에 방문처리를 해주고 queue에 저장한ㄷ.

계속해서 pop해온 위치에서 사다리나 뱀을 찾았는데 애초에 문제에 나온 순서가 그게아님
그리고 일단 사다리나 뱀이 나오면 무조건 그곳으로 이동해야함 이동하지 않는다는 조건 X
"""
def playDice():
    visit = [-1] * 101
    visit[1] = 0
    q = [1]
    while q:
        pst = q.pop(0)
        for i in range(1, 7):
            move = pst + i
            if move <= 100:
                if move == 100:
                    return visit[pst] + 1
                if move in ladder.keys() and visit[move] == -1:
                    visit[move] = 0
                    move = ladder[move]
                if visit[move] == -1:
                    visit[move] = visit[pst] + 1
                    q.append(move)

res = playDice()
print(res)
