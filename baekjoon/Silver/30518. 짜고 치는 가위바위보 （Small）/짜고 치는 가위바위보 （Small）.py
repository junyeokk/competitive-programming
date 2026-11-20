import sys
input = sys.stdin.readline

lig = input().strip()
sma = input().strip()
n = len(sma)

def lig_win(l, s):
    if (l == "R" and s == "S") or (l == "S" and s == "P") or (l == "P" and s == "R"):
        return True
    else:
        return False
cnt = 0

for i in range(1, 2 ** n):
    valid = True
    flag = False
    prev = -1
    
    for j in range(n):
        if i & (1 << j):
            if prev == -1:
                flag = lig_win(lig, sma[j])
            else:
                if flag and sma[prev] == sma[j]:
                    valid = False
                    break
                flag = lig_win(sma[prev], sma[j])
            prev = j

    if valid:
        cnt += 1

print(cnt)