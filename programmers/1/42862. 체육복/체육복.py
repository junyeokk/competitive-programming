def solution(n, lost, reserve):
    ls = set(lost)
    rs = set(reserve)
    
    os = ls & rs
    ls = ls - os
    rs = rs - os
    
    answer = n - len(ls)

    for x in sorted(ls):
        if (x - 1) in rs:
            rs.remove(x - 1)
            answer += 1
        elif (x + 1) in rs:
            rs.remove(x + 1)
            answer += 1
    
    return answer