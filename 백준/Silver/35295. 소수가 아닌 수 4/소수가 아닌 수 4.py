n = int(input())

s = list(map(int, input().split()))

s.sort()

s1 = False
for i in range(2, int(s[1] ** 0.5) + 1):
    if s[1] % i == 0:
        s1 = True


if len(s) == 2 and not s1 and s[0] == 1:
    print("NO")
else:
    print("YES")
    print(2)
    print(s[-1], s[-2])