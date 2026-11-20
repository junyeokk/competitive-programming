from collections import defaultdict

tc = int(input())

def max_allowed(rank):
    if rank <= 10:
        return 3
    elif rank <= 20:
        return 2
    elif rank <= 30:
        return 1
    else:
        return 0

def solve():
    t = []
    total_teams = defaultdict(int)
    total_count = defaultdict(int)
    res = []
    res_temp = []

    n = int(input())
    for i in range(n):
        s = list(map(str, input().split()))
        s[2] = int(s[2])
        s[3] = int(s[3])
        t.append(s)
    
    for i in t:
        total_teams[i[1]] += 1
    
    for rank, team in enumerate(t, 1):
        school = team[1]
        if (total_count[school] < (total_teams[school] + 1) // 2 
            and total_count[school] <= max_allowed(rank)):
            res.append(team)
            if len(res) >= 60:
                break
            total_count[school] += 1
        else:
            res_temp.append(team)
    
    if len(res) < 60:
        need = 60 - len(res)
        res += res_temp[:need]
    
    for team in reversed(t):
        if team in res:
            print(team[0])
            break

for _ in range(tc):
    solve()