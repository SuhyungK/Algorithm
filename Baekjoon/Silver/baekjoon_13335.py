# 트럭

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

def move():
    queue = [0] * w
    sumW = time = next = 0
    while True:
        time += 1

        # 다리 가장 앞에 있는 트럭을 내리며 동시에 다리 위 무게 총합(sumW)에서 제거
        # 트럭이 아닌 경우에는 그냥 0이 제거된다
        sumW -= queue.pop(0)

        # 다음 트럭이 존재한다면 sumW에 다음 트럭이 올라올 수 있는지 판단
        # 올라올 수 있다면 무게를 더해주고, 트럭을 다리에 올린다
        # 이제 다리에 올라오지 않은 다음 트럭으로 next는 옮겨간다
        if next < n and sumW + (trc:=truck[next]) <= L:
            sumW += trc
            queue.append(trc)
            next += 1
        # 만약 안 된다면, 아무것도 올리지 않는다(0)
        else:
            queue.append(0)

        # 다리 위에 아무 트럭도 올라와 있지 않고 더 올라올 트럭도 없다면 종료한다
        if not sumW and next == n:
            return time

print(move())