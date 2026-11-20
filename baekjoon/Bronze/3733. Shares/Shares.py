import sys
data = sys.stdin.read().split()

for i in range(0, len(data), 2):
    n, s = int(data[i]), int(data[i + 1])
    print(s // (n + 1))