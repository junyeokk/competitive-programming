arr = list(map(int, input().split()))
visit = [0 for i in range(10)]
chk = 0

def comb(idx):
    if idx == 10:
        s = 0
        for i in range(10):
            if visit[i] == 1:
                s += arr[i]
        if s == 100:
            global chk
            chk = 1
            for i in range(10):
                if visit[i] == 1:
                    print(arr[i], end=' ')
            print()
        return
    
    visit[idx] = 1
    comb(idx + 1)
    visit[idx] = 0
    comb(idx + 1) 

comb(0)
if chk == 0:
    print(-1)