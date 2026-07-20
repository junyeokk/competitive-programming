def solution(n, computers):
    visit = [0 for i in range(n + 1)]
    
    def dfs(node):
        visit[node] = 1
        for j in range(n):
            if computers[node][j] == 1 and not visit[j]:
                dfs(j)
    
    answer = 0
    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1

    return answer