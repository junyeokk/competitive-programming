n = input()
intn = int(n)
length = len(n)
visit = [0 for i in range(length)]
ans = []
v = 1000000

def perm(idx):
    global v
    if idx == length:
        s = ''
        for i in range(length):
            s += n[ans[i]]
        s = int(s)
        if intn < s:
            v = min(v, s)
        return

    for i in range(length):
        if visit[i] == 0:
            visit[i] = 1
            ans.append(i)
            perm(idx + 1)
            ans.pop()
            visit[i] = 0

perm(0)
if v == 1000000:
    v = 0
print(v)