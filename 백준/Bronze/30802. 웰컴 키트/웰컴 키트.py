n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
tcnt = 0

for s in size:
    if s % t == 0:
        tcnt += s // t
    else:
        tcnt += (s // t) + 1

print(tcnt)
print(n // p, n % p)