from collections import deque

q = deque()

visit = [0 for _ in range(200001)]

s = int(input())
e = int(input())

visit[s] = 1
q.append([s, 0])

while q:
    pos, time = q.popleft()

    if pos == e:
        print(time)
        break
    
    for next_pos in [pos - 1, pos + 1, pos * 2, pos * 3]:
        if 0 <= next_pos <= 200000 and visit[next_pos] == 0:
            visit[next_pos] = 1
            q.append([next_pos, time + 1])