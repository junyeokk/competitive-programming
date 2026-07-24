def solution(board, skill):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    diff = [[0] * m for _ in range(n)]
    
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        delta = degree if type == 2 else -degree
        
        diff[r1][c1] += delta # 왼쪽 위 모서리
        if c2 + 1 < m:
            diff[r1][c2 + 1] -= delta # 오른쪽 위 모서리
        if r2 + 1 < n:
            diff[r2 + 1][c1] -= delta # 왼쪽 아래 모서리
        if r2 + 1 < n and c2 + 1 < m: # 오른쪽 아래 모서리
            diff[r2 + 1][c2 + 1] += delta
            
    # 누적합
    for r in range(n):
        for c in range(1, m):
            diff[r][c] += diff[r][c - 1] # 가로 누적합

    for c in range(m):
        for r in range(1, n):
            diff[r][c] += diff[r - 1][c]

    for r in range(n):
        for c in range(m):
            if board[r][c] + diff[r][c] >= 1:
                answer += 1
        
    return answer