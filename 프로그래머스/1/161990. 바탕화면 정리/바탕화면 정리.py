def solution(wallpaper):
    answer = []
    
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    lux, luy = n, m
    rdx, rdy = -1, -1
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx + 1)
    answer.append(rdy + 1)
    
    return answer