from collections import deque

n = int(input())
k = int(input())
apple = set()

for i in range(k):
    y, x = map(int, input().split())
    apple.add((x, y))


snake = set()
q = deque()
q.append((1, 1))
snake.add((1, 1))
v = (1, 0)
rotate = {
    (1, 0): {'L' : (0, -1), 'D': (0, 1)},
    (-1, 0): {'L': (0, 1), 'D': (0, -1)},
    (0, 1): {'L': (1, 0), 'D': (-1, 0)},
    (0, -1): {'L': (-1, 0), 'D': (1, 0)}
}

L = int(input())
pre = 0
t = 0
gameOver = False
for i in range(L):
    X, C = input().split()
    X = int(X)
    for j in range(X - pre):
        t += 1
        x, y = q[-1]
        nx = x + v[0]
        ny = y + v[1]
        if (nx, ny) in snake:
            gameOver = True
            break

        if nx < 1 or ny < 1 or nx > n or ny > n:
            gameOver = True
            break
        
        if (nx, ny) in apple:
            apple.remove((nx, ny))
        else:
            r = q.popleft()
            snake.remove(r)
        q.append((nx, ny))
        snake.add((nx, ny))

    if gameOver:
        break
    pre = X
    v = rotate[v][C]

while not gameOver:
    t += 1
    x, y = q[-1]
    nx = x + v[0]
    ny = y + v[1]
    if (nx, ny) in snake:
        gameOver = True
        break
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        gameOver = True
        break
    if (nx, ny) in apple:
        apple.remove((nx, ny))
    else:
        r = q.popleft()
        snake.remove(r)
    q.append((nx, ny))
    snake.add((nx, ny))
print(t)    