n, m = map(int, input().split())

is_prime = [True] * 2000001
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(2000000 ** 0.5)):
    if is_prime[i]:
        for j in range(i * 2, 2000001, i):
            is_prime[j] = False

base = 1
while True:
    flag = True
    s = base
    for j in range(n):
        if is_prime[s]:
            base += 1
            flag = False
            break
        s += m
    if flag:
        break

res = base
for i in range(n):
    print(res, end = ' ')
    res += m