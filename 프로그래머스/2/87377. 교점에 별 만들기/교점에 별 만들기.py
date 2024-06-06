def solution(line):
    pos, answer = [], []
    n = len(line)
    
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
    
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)
    
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]
    
    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'
    
        
    for result in coord: answer.append(''.join(result))
    
    return answer[::-1]
    
    return answer;