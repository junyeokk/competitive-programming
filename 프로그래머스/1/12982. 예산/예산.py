def solution(d, budget):
    tot = 0
    answer = 0
    
    d.sort()
    for t in d:
        if tot + t > budget:
            break
        tot += t
        answer += 1
    
    return answer