def solution(users, emoticons):
    answer = []

    lst = [40, 30, 20, 10]
    emoticons.sort(reverse=1)
    for sale in product(lst, repeat=len(emoticons)):
        signin = total_price = 0
        for percent, price in users:
            user_price = 0
            for i in range(len(sale)):
                if sale[i] < percent:
                    continue

                user_price += emoticons[i] * (1-0.01*sale[i])
                if user_price >= price:
                    signin += 1
                    break
            else:
                total_price += user_price

            answer = max(answer, [signin, total_price])
    return answer

from itertools import product