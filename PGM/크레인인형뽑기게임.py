def solution(board, moves):
    ans, stk = 0, [0]
    dolls = list(map(lambda x: [0] + list(filter(lambda y: y > 0, x)), zip(*board[::-1])))
    
    for move in moves:
        move -= 1
        if (doll:=dolls[move][-1]) > 0:
            if stk[-1] == doll:
                stk.pop()
                ans += 2
            else:
                stk.append(doll)
            dolls[move].pop()
            
    return ans

if __name__ == '__main__':
    solution([[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0], [1, 2, 2, 1]], [2, 3, 1, 4, 2, 3])