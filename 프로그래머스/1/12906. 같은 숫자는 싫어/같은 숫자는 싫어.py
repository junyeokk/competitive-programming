def solution(arr):
    answer = []
    
    idx = 0
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != answer[idx]:
            answer.append(arr[i])
            idx += 1        
    
    return answer