def solution(user_id, banned_id):
	# 불량 아이디에 해당하는 응모자 아이디인지 확인
    def find(ban, user):
        if len(ban) != len(user):
            return []

        lst = list(map(set, zip(ban, user)))
        for i in lst:
            if len(i) != 1 and '*' not in i:
                return []

        return [user]
	
    # 불량 아이디에 해당하는 응모자 아이디들 찾기
    def find_banned_users_lst():
        banned_users_lst, banned_lst = defaultdict(list), []*len(banned_id)
        for ban in banned_id:
            if not banned_users_lst[ban]:
                for user in user_id:
                    banned_users_lst[ban] += find(ban, user)
            banned_lst.append(banned_users_lst[ban])

        return banned_lst
	
    # 가능한 조합 만들기(재귀)
    def make_combination(lst, idx, comb):
        nonlocal answer
        if idx == len(lst):
            answer.append(" ".join(sorted(comb)))
            return 

        for i in lst[idx]:
            if i not in comb:

                make_combination(lst, idx+1, comb+[i])                

    answer = []
    make_combination(find_banned_users_lst(), 0, [])
    return len(set(answer))

from collections import defaultdict