def solution(targets):
    answer = 1

    targets.sort()
    s1, e1 = targets[0]

    for s2, e2 in targets[1:]:
        if s2 < e1 and s1 < e2:
            s1, e1 = s2, min(e1, e2)
        else:
            answer += 1
            s1, e1 = s2, e2
    return answer