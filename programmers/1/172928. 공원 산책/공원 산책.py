def solution(park, routes):
    answer = []
    xpos, ypos = 0, 0
    delta = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                xpos, ypos = i, j
    
    for r in routes:
        op, n = r.split(' ')
        dr, dc = delta[op]
        n = int(n)
        nr, nc = xpos, ypos
        
        valid = True
        for i in range(1, n + 1):
            nr, nc = xpos + dr * i, ypos + dc * i
            if nr < 0 or nc < 0 or nr >= len(park) or nc >= len(park[0]):
                valid = False
                break
            if park[nr][nc] == 'X':
                valid = False
                break

        if valid:
            xpos, ypos = nr, nc
    
    answer.append(xpos)
    answer.append(ypos)
        
    return answer