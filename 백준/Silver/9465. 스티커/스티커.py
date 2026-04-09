t = int(input())

def solve():
    n = int(input())
    sc1 = list(map(int, input().split()))
    sc2 = list(map(int, input().split()))

    top = sc1[0]
    bot = sc2[0]
    none = 0

    for i in range(1, n):
        new_top = max(bot, none) + sc1[i]
        new_bot = max(top, none) + sc2[i]
        new_none = max(top, bot, none)
        top, bot, none = new_top, new_bot, new_none
    
    print(max(top, bot, none))

for i in range(t):
    solve()