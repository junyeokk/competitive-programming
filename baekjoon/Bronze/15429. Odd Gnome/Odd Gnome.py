t = int(input())

def solve():
    s = list(map(int, input().split()))
    idx = -1
    gcnt = s[0]
    gnome = s[1:]
    
    for i in range(1, len(gnome) - 1):
        if gnome[i + 1] - gnome[i - 1] == 1:
            idx = i
            break

    print(idx + 1)

for i in range(t):
    solve()