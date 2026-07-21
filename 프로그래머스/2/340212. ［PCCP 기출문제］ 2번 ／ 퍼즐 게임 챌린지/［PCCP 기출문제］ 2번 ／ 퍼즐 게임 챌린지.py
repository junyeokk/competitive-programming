def calc_time(level, diffs, times):
    ttime = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            ttime += times[i]
        elif diffs[i] > level:
            ttime += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
    return ttime

def solution(diffs, times, limit):
    answer = 0
    
    low, high = 1, max(diffs)
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if calc_time(mid, diffs, times) <= limit:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer