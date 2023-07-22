def solution(picks, minerals):
    answer = 1e9
    
    name = {
        "diamond": 0, "iron": 1, "stone":2
    }
    info = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    
    # 다이아, 철, 돌 곡괭이, 캐야 하는 광물 인덱스, 피로도
    def mining(dia, iron, stone, idx, fatigue):
        nonlocal answer
        if idx >= len(minerals) or dia == iron == stone == 0:
            answer = min(answer, fatigue)
            print(fatigue)
            return 
        
        if dia:
            temp = 0
            for m in minerals[idx:idx+5]:
                temp += info[0][name[m]]
            mining(dia-1, iron, stone, idx+5, fatigue+temp)
        
        if iron:
            temp = 0
            for m in minerals[idx:idx+5]:
                temp += info[1][name[m]]
            mining(dia, iron-1, stone, idx+5, fatigue+temp)
        
        if stone:
            temp = 0
            for m in minerals[idx:idx+5]:
                temp += info[2][name[m]]
            mining(dia, iron, stone-1, idx+5, fatigue+temp)
    
    mining(*picks, 0, 0)
    return answer