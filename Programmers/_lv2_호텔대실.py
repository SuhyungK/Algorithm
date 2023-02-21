def solution(book_time):
    
    bt_lst = []
    for bt in book_time:
        st, et = map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), bt)
        bt_lst.append((st, et+10))
    bt_lst.sort(key=lambda x: (x[1], x[0]))

    rooms = []
    for bt in bt_lst: 
        for room in rooms:
            if room[1]:
        room.append(bt)

    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# print(solution([["17:00", "19:00"], ["16:40", "19:00"]]))