def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries or pickups:

        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        answer += max(len(deliveries)*2, len(pickups)*2)

        limit = cap
        while deliveries and limit:
            if deliveries[-1] >= limit:
                deliveries[-1] -= limit
                break
            limit -= deliveries.pop()

        limit = 0
        while pickups and limit < cap:
            if pickups[-1] >= cap-limit:
                pickups[-1] -= cap-limit
                break
            limit += pickups.pop()

    return answer