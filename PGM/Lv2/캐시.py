def solution(cacheSize, cities):
    answer = 0

    used = dict()
    top = 0
    queue = [0] * cacheSize
    for idx, city in enumerate(map(lambda x: x.lower(), cities), 1):
        answer += 1
        
        # 도시 이름이 캐시에 존재할 때
        # 참조 시기만 업데이트
        if used.get(city):
            used[city] = idx
            continue

        # 도시 이름이 캐시에 존재하지 않지만 캐시가 비어 있을 때
        answer += 4
        if top != cacheSize:
            queue[top] = city
            used[city] = idx
            top += 1
            continue
        
        # 캐시 크기가 0이 아닐 때
        # 캐시를 돌면서 가장 예전에 사용됐던 도시 이름을 제거하고
        # 그 자리에 현재 도시 이름을 넣고 참조 시기 업데이트
        if queue:
            least, minValue = 51, 100001
            for header in range(cacheSize):
                if used[queue[header]] < minValue:
                    least = header
                    minValue = used[queue[header]]

            used[queue[least]] = 0
            queue[least] = city
            used[city] = idx

    return answer