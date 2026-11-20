n = int(input())

stack = []
res = []
arr = list(map(int, input().split()))

arr.reverse()

for v in arr:
    while stack and stack[-1] <= v:
        stack.pop()

    if not stack:
        res.append(0)
    else:
        res.append(stack[-1])
    
    stack.append(v)

res.reverse()

for r in res:
    print(r, end = ' ')