from collections import defaultdict

def solution(N, stages):
    answer = []
    d = defaultdict(int)
    
    for s in stages:
        d[s] += 1
    
    r = len(stages) # remaining
    for i in range(1, N + 1):
        stu = d[i]
        
        if r == 0:
            rate = 0
        else:
            rate = stu / r
        
        answer.append((i, rate))
        r -= stu
    
    answer = sorted(answer, key=lambda x:x[1], reverse=True)
    
    s = []
    for a in answer:
        s.append(a[0])
    
    return s