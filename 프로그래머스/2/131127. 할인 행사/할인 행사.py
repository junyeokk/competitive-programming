from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    s = []
    
    for i in range(len(want)):
        for j in range(number[i]):
            s.append(want[i])
    
    wc = Counter(s)
    
    for i in range(len(discount) - 9):
        t = discount[i:i + 10]
        tc = Counter(t)
        if wc == tc:
            answer += 1
    
    return answer