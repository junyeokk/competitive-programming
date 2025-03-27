from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
  x, y = map(int, input().split())
  points.append((x, y))

x_count = defaultdict(int)
y_count = defaultdict(int)

for x, y in points:
  x_count[x] += 1
  y_count[y] += 1

total_lines = 0

for count in x_count.values():
  if count >= 2:
    total_lines += 1

for count in y_count.values():
  if count >= 2:
    total_lines += 1

print(total_lines)