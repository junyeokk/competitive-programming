def solution(sizes):
    h = -1
    w = -1
    
    for s in sizes:
        s.sort()
    
    for mh, mw in sizes:
        if h < mh:
            h = mh
        if w < mw:
            w = mw
    
    return h * w