def solution(board, moves):
    answer = 0
    stk = []
    
    for t in moves:
        for i in range(len(board)):
            if board[i][t - 1]:
                stk.append(board[i][t - 1])
                board[i][t - 1] = 0
                if len(stk) >= 2 and stk[-1] == stk[-2]:
                    stk.pop()
                    stk.pop()
                    answer += 2
                break
                
    
    return answer