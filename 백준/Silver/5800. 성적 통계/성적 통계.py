t = int(input())
cnt = 1

def solve():
    global cnt
    s = list(map(int, input().split()))
    score = s[1:]

    smax = max(score)
    smin = min(score)
    score = sorted(score)
    lgap = -1
    
    for i in range(len(score) - 1):
        if score[i + 1] - score[i] > lgap:
            lgap = score[i + 1] - score[i]

    print(f'Class {cnt}')
    print(f'Max {smax}, Min {smin}, Largest gap {lgap}')
    cnt += 1

for i in range(t):
    solve()