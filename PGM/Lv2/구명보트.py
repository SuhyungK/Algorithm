def solution(people, limit):
    answer = 0
    
    # 가벼운 것 → 무거운 것 순서로 정렬
    people.sort()
    
    light, heavy = 0, len(people)-1
    
    # 무거운 것 + 가벼운 것의 무게가 limit을 넘으면 둘 다 태우고
    # 넘지 못하면 무거운 것만 태움
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
    return answer