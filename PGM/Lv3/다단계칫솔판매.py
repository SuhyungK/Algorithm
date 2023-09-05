def solution(enroll, referral, seller, amount):
    parent = defaultdict(lambda: '')
    profit = defaultdict(int)
   
    # 부모-자식 정보 저장
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
    
    # 반복문으로 자식에서 10%씩 부모에게 전달
    for j in range(len(seller)):
        i_amount = amount[j]*100
        i_seller = seller[j]
        while True:
            rem = int(i_amount*0.1)
            profit[i_seller] += i_amount-rem
            if not parent[i_seller] or not rem:
                break
                
            i_amount, i_seller = rem, parent[i_seller]
    
    answer = []
    for name in enroll:
        answer.append(profit[name])
    
    return answer
from collections import defaultdict