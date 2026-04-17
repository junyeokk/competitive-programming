a, b = map(int, input().split())

la = set(map(int, input().split()))
lb = set(map(int, input().split()))

res = sorted(la - lb)
if len(res) > 0:
    print(len(res))
    print(*res)
else:
    print(0)