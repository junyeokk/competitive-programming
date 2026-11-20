n, m, a, b = map(int, input().split())
res = 0

timetable = list(map(int, input().split()))
like = set(map(int, input().split()))
like_len = 0
dislike = set(map(int, input().split()))
dislike_len = 0

for tidx in range(n):
    if timetable[tidx] in like:
        like_len += 1
        if dislike_len >= 3:
            res -= dislike_len
        dislike_len = 0
    elif timetable[tidx] in dislike:
        dislike_len += 1
        if like_len >= 3:
            res += like_len
        like_len = 0        
    else:
        if like_len >= 3:
            res += like_len
        if dislike_len >= 3:
            res -= dislike_len
        like_len = 0
        dislike_len = 0

if like_len >= 3:
    res += like_len
if dislike_len >= 3:
    res -= dislike_len

print(res)