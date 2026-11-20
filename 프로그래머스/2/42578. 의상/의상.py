from collections import defaultdict

def solution(clothes):
    cnt = 1
    s = defaultdict(list)
    for k, v in clothes:
        s[v].append(k)
    
    for k, v in s.items():
        cnt *= (len(v) + 1)
    cnt -= 1
    
    return cnt