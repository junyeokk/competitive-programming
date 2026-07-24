def solution(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]
    
    for r in range(1, n):
        for c in range(len(triangle[r])):
            if c == 0:
                dp[r][c] = triangle[r][c] + dp[r - 1][c]
            elif c == r:
                dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]
            else:
                dp[r][c] = triangle[r][c] + max(dp[r - 1][c - 1], dp[r - 1][c])

    return max(dp[-1])