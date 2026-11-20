def solution(number, k):
    s = []
    for d in number:
        while s and k > 0 and s[-1] < d:
            s.pop()
            k -= 1
        s.append(d)
    
    if k > 0:
        return ''.join(s[:len(s) - k])
    
    return ''.join(s)