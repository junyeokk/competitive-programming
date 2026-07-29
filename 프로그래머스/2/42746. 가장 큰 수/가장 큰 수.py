from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    t = []
    
    for n in numbers:
        t.append(str(n))
    
    s = sorted(t, key = cmp_to_key(compare))
    
    res = ''.join(s)
    if res[0] == '0':
        return '0'
    return res