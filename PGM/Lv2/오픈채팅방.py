def solution(record):
    _record = [re.split() for re in record]
    
    chats, uuid = [], {}
    for do, *user in _record:
        if do == "Enter":
            uuid[user[0]] = user[1]
            chats.append(['E', user[0]])
        elif do == "Leave":
            chats.append(['L', user[0]])
        else:
            uuid[user[0]] = user[1]
    
    answer = []
    for do, user in chats:
        if do == 'E':
            answer.append(f"{uuid[user]}님이 들어왔습니다.")
        else:
            answer.append(f"{uuid[user]}님이 나갔습니다.")
            
    return answer