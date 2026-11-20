def solution(s):
    answer = ''
    ls = s.split(' ')
    lsn = []
    
    for ss in ls:
        lsn.append(int(ss))
    
    ml = min(lsn)
    mx = max(lsn)
    
    return ' '.join((str(ml), str(mx))) 