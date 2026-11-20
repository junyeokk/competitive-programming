def solution(points, routes):
    answer = 0
    p = []
    
    for route in routes:
        ls = []
        for j in range(len(route) - 1):
            start = points[route[j] - 1]
            end = points[route[j + 1] - 1]
            r, c = start[0], start[1]
            er, ec = end[0], end[1]

            if j == 0:
                ls.append((r, c))
            while (r, c) != (er, ec):
                if r != er:
                    r += 1 if r < er else -1
                else:
                    c += 1 if c < ec else -1
                ls.append((r, c))
        p.append(ls)
    
    max_t = max(len(robot) for robot in p)
    for t in range(max_t):
        pos = []
        for i in range(len(p)):
            if t < len(p[i]):
                pos.append(p[i][t])
        
        for coord in set(pos):
            if pos.count(coord) >= 2:
                answer += 1
    
    return answer


