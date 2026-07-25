def solution(n, times):
    lo = min(times)
    hi = max(times) * n
    
    def ttime(T, times):
        tot = 0
        for t in times:
            tot += T // t
        return tot
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if ttime(mid, times) >= n:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return lo