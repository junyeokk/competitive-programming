import re

def solution(files):
    t = []
    answer = []
    
    for f in files:
        match = re.match(r'([^0-9]+)([0-9]+)(.*)', f)
        head = match.group(1)
        number = match.group(2)
        tail = match.group(3)
        t.append((head.lower(), int(number), f))
    
    t = sorted(t, key=lambda x:(x[0], x[1]))
    
    for s in t:
        answer.append(s[2])
    
    return answer