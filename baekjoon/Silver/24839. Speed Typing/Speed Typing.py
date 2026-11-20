t = int(input())

def solve(tc):
    # ip = 0
    pp = 0

    i = input()
    p = input()

    for ipc in i:
        while pp < len(p) and p[pp] != ipc:
            pp += 1
        if pp == len(p):
            print(f'Case #{tc + 1}: IMPOSSIBLE')
            return
        pp += 1
    
    print(f'Case #{tc + 1}: {len(p) - len(i)}')

for i in range(t):
    solve(i)