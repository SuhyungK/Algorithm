def solution(arr):
    answer = []
    answer.append(arr[0])

    for a in arr[1:]:
        if a != answer[-1]:
            answer.append(a)

    return answer

# 다시 풀기




# 풀이
def solution(arr):
    answer = []

    for a in arr:
        if [a] != answer[-1:]:
            answer.append(a)
            print(answer[-1:], a)

    return answer
