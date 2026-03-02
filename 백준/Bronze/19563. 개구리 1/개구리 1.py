a, b, c = map(int, input().split())
m = abs(a) + abs(b)

if m == c:
    print("YES")
elif m < c and (c - abs(a) - abs(b)) % 2 == 0:
    print("YES")
else:
    print("NO")