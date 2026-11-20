def solution(citations):
    answer = 0
    c = sorted(citations, reverse=True)
    
    for i in range(len(c)):
        if c[i] >= i + 1:
            answer += 1
        else:
            break
    
    return answer