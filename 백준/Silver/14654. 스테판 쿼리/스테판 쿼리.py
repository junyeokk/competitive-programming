n = int(input())

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

streak = 0
max_streak = 0
prev_winner = 0

# 1: 가위, 2: 바위, 3: 보
# return 0: 비김 return 1: 1팀 승, return 2: 2팀 승
def rsp(res):
    if res == (2, 1) or res == (3, 2) or res == (1, 3):
        return 1
    elif res == (1, 2) or res == (2, 3) or res == (3, 1):
        return 2
    else:
        return 0

for i in range(n):
    winner = rsp((t1[i], t2[i]))

    if winner == 0:
        winner = 3 - prev_winner
    if winner == prev_winner:
        streak += 1
    else:
        streak = 1
        prev_winner = winner
    
    max_streak = max(streak, max_streak)

print(max_streak)