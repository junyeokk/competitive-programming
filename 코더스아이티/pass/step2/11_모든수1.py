a, b = map(int, input().split())
ans = [0 for i in range(a)]

def perm(idx):
    if idx == a:
        print(ans)
        return
    
    for i in range(b):
        ans[idx] = i + 1
        perm(idx + 1)

perm(0)