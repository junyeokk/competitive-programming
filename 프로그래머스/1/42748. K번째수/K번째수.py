def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c
        ta = sorted(array[i - 1:j])
        answer.append(ta[k - 1])
        
    return answer