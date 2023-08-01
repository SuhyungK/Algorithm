def solution(k, dungeons):
    answer = -1

    for perm in permutations(dungeons, len(dungeons)):
        count, now_k = 0, k
        for min_k, consume in perm:
            if now_k >= min_k:
                now_k -= consume
                count += 1

        answer = max(answer, count)

    return answer

from itertools import permutations