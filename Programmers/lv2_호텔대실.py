def recycle_room(hotel_room):
    room_lst = [0]
    l = len(hotel_room)
    i = 0
    while i < l:
        print('room_lst', room_lst)
        for j in range(i+1, l):
            if hotel_room[i][1] <= hotel_room[j][0]:
                i = j
                room_lst.append(j)
                break
        else: 
            i += 1

    for used in room_lst[::-1]:
        hotel_room.pop(used)
        
    return hotel_room
    
def solution(book_time):
    
    bt_lst = []
    for bt in book_time:
        st, et = map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), bt)
        bt_lst.append((st, et))
    
    bt_lst.sort(key=lambda x: x[1])
    
    room_cnt = 0
    while bt_lst:
        bt_lst = recycle_room(bt_lst)
        room_cnt += 1

    return room_cnt 

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))