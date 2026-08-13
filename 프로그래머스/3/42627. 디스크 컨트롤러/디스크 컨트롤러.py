import heapq

def solution(jobs):
    t = 0
    hq = []
    using = False
    curT = 0
    tot = 0
    succ = 0
    
    while True:
        for j in jobs:
            if t == j[0]:
                heapq.heappush(hq, [j[1], j[0]])
        
        if using and curT == 0:
            using = False
            tot += t - cur[1]
            succ += 1
        
        if hq and not using:
            cur = heapq.heappop(hq)
            curT = cur[0]
            using = True

        if succ == len(jobs):
            return tot // len(jobs)
        
        t += 1
        curT -= 1