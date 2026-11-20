from math import lcm

def solution(signals):
    p = [g + y + r for g, y, r in signals]
    a = p[0]
    for r in p[1:]:
        a = lcm(a, r)
    
    for i in range(1, a + 1):
        ay = True
        for j in range(len(signals)):
            g, y, r = signals[j]
            pos = (i - 1) % (g + y + r)
            if not (g <= pos < g + y): # 노란 불이 아니면
                ay = False
                break
        if ay:
            return i
    
    return -1