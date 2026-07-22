def solution(numbers, target):
    answer = 0
    
    def dfs(idx, tot):
        nonlocal answer
        
        if idx == len(numbers):
            if tot == target:
                answer += 1
            return
        dfs(idx + 1, tot + numbers[idx])
        dfs(idx + 1, tot - numbers[idx])
    
    dfs(0, 0)
    return answer