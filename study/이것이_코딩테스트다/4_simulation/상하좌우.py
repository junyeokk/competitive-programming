n = int(input())
a, b = 1, 1
moves = input().split()
nx = 0
ny = 0

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
lrud = ['L', 'R', 'U', 'D']

for move in moves:
  for i in range(4):
    if lrud[i] == move:
      nx = a + dx[i]
      ny = b + dy[i]
    if nx >= 1 and nx < n and ny >= 1 and ny < n:
      a, b = nx, ny

print(a, b)
