def solution(today, terms, privacies):
    answer = []
    d = {}
    
    def to_days(y, m, day):
        return y * 12 * 28 + m * 28 + day
    
    ty, tm, td = map(int, today.split('.'))
    today_days = to_days(ty, tm, td)
    
    for t in terms:
        a, b = t.split(' ')
        d[a] = int(b)
    

    for idx, p in enumerate(privacies, 1):
        date, term = p.split(' ')
        yyyy, mm, dd = map(int, date.split('.'))
        expiry_days = to_days(yyyy, mm, dd) + d[term] * 28 - 1
        
        # 파기
        if today_days > expiry_days:
            answer.append(idx)
            
    return answer