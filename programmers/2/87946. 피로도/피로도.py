from itertools import permutations

def solution(k, dungeons):
    best = -9999999
    
    for order in permutations(dungeons):
        cnt = 0
        cur = k
        for mns, us in order:
            if mns <= cur:
                cur -= us
                cnt += 1
        best = max(best, cnt)
    
    return best