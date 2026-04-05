from collections import defaultdict

d = defaultdict(int)

n = int(input())
s = input().split()

for i in range(n):
    if s[i].endswith('Cheese'):
        d[s[i]] += 1

if len(d) >= 4:
    print("yummy")
else:
    print("sad")