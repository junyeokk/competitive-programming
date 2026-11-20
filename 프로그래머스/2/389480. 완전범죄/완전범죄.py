def solution(info, n, m):
    dp = [float('inf') for _ in range(n)]
    dp[0] = 0
    
    for acost, bcost in info:
        ndp = [float('inf')] * len(dp)
        for a in range(len(dp)):
            if dp[a] == float('inf'):
                continue
            if a + acost < n:
                ndp[a + acost] = min(ndp[a + acost], dp[a])
            if dp[a] + bcost < m:
                ndp[a] = min(ndp[a], dp[a] + bcost)
        dp = ndp
    
    for a in range(n):
        if dp[a] != float('inf'):
            return a

    return -1