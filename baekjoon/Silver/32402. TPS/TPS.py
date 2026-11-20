n = int(input())

px, py = 0, 0 # 플레이어 위치
dx, dy = 0, 1 # 방향

for i in range(n):
    s = input()
    if s == 'W': px += dx; py += dy
    elif s == 'A': px -= dy; py += dx
    elif s == 'S': px -= dx; py -= dy
    elif s == 'D': px += dy; py -= dx
    elif s == 'MR': dx, dy = dy, -dx
    elif s == 'ML': dx, dy = -dy, dx
    print(px, py, px - dx, py - dy)